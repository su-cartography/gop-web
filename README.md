# Gallery of Possibilities

A feminist map icon gallery website and API for the QGIS plugin.

This repo is a place to store, browse, upload, and manage map icons. The website and the QGIS plugin will both use the same backend.

## Team

| Area | Focus |
|------|--------|
| Backend / database | Django, PostgreSQL, APIs, file storage |
| Frontend | React UI, gallery, forms, pages |

## Stack

- **Frontend:** React (Vite)
- **Backend:** Django + Django REST Framework
- **Database:** PostgreSQL

## Repo layout

| Path | Purpose |
|------|---------|
| `backend/` | Django API and admin |
| `frontend/` | React app |

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL

## Backend setup

### 1. Create the database

In pgAdmin (or `psql`), create a PostgreSQL database named `gop`.

### 2. Configure environment variables

```bash
cd backend
copy .env.example .env
```

On macOS/Linux use `cp .env.example .env` instead.

Edit `.env` and set:

- `SECRET_KEY` — any long random string
- `DB_PASSWORD` — your local PostgreSQL password
- `DB_USER` — usually `postgres` (change if you use another user)

Do **not** commit `.env`.

### 3. Install dependencies and run

```bash
cd backend
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**macOS / Linux:**

```bash
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Will be at [http://127.0.0.1:8000/].

## Frontend setup

Requires Node.js 18+. The Vite proxy is already configured so `/api` and `/media` go to Django on port 8000.

```bash
cd frontend
npm install
npm run dev
```

The app will be at [http://127.0.0.1:5173/].

Keep Django running on port 8000 in another terminal so API and media requests work.

## Running both together

1. Start the backend: `python manage.py runserver` (in `backend/`, venv active).
2. Start the frontend: `npm run dev` (in `frontend/`).
3. Use the site at [http://127.0.0.1:5173/](http://127.0.0.1:5173/).

## Notes

- Icon metadata will live in PostgreSQL; PNG/SVG files under `backend/media/` (later).
- Prefer not committing large icon files under `media/`.
- Frontend calls should use paths like `/api/...` so the Vite proxy can forward them to Django.
