# 🚀 Universal Boilerplate Generator

A dynamic web-based utility built with **Django** that helps developers instantly generate structured project boilerplates. Instead of manually creating folders and configuration files, users can select their desired tech stack and download a ready-to-code project bundle as a `.zip` file.

## 🛠️ Tech Stack
* **Backend:** Python 3.10+, Django 4.2+
* **Database:** PostgreSQL (for production-ready logic)
* **Frontend:** HTML5, Tailwind CSS (via CDN)
* **Utilities:** `zipfile` for dynamic bundling, `secrets` for secure key generation.

## ✨ Key Features
* **Dynamic Scaffolding:** Generates real project structures based on user input.
* **Search-and-Replace Engine:** Automatically injects the chosen `project_name` and unique `SECRET_KEY` into the boilerplate files.
* **Smart Requirements:** Dynamically adds libraries like `psycopg2-binary` only if the user selects PostgreSQL support.
* **Modern UI:** A clean, responsive "glassmorphism" interface built with Tailwind CSS.

## 📂 Project Structure
```text
├── config/             # Django project settings
├── core_generator/     # Main application logic
│   ├── blueprints/     # Raw template files (Skeletons)
│   │   └── django_standard/
│   ├── templates/      # Dashboard and Wizard UI
│   └── views.py        # Zipping and replacement logic
├── venv/               # Virtual environment
└── manage.py           # Django CLI
