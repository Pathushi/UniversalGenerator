# Create your views here.
import io
import zipfile
import os
import secrets
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def generate_zip(request):
    if request.method == "POST":
        proj_name = request.POST.get('project_name', 'my_new_project')
        use_postgres = request.POST.get('use_postgres') # Check if box was ticked
        
        # Generate a random secret key for the new project
        secret_key = secrets.token_urlsafe(32)
        
        # Logic for extra libraries
        extra_libs = ""
        if use_postgres:
            extra_libs = "psycopg2-binary"

        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zf:
            base_path = os.path.join(os.path.dirname(__file__), 'blueprints/django_standard')
            
            for root, dirs, files in os.walk(base_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, base_path)

                    with open(file_path, 'r') as f:
                        content = f.read()
                    
                    # --- DYNAMIC REPLACEMENTS ---
                    content = content.replace('{{ project_name }}', proj_name)
                    content = content.replace('{{ secret_key }}', secret_key)
                    content = content.replace('{{ extra_libraries }}', extra_libs)
                    
                    zf.writestr(rel_path, content)

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={proj_name}.zip'
        return response

    