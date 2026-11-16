# Pravin Bansode — Interactive Room Portfolio

A Django portfolio website with a separate FastAPI JSON API, PostgreSQL support, responsive HTML/CSS/JavaScript, uploadable profile photo, and a study-material gallery.

## Stack
- Django 5.2: portfolio pages, admin, contact form, profile/gallery management
- FastAPI: JSON API endpoints
- PostgreSQL: production database (SQLite fallback for local quick start)
- HTML, CSS, vanilla JavaScript
- Render: deploy Django and FastAPI as separate web services with one PostgreSQL database

## Important asset note
`static/img/portfolio-room.png` is a clean room-only background with no portfolio UI, navigation, labels, or text baked into the image. The website content is separate HTML/CSS, and section navigation appears in its own section below the room so it does not collide with furniture or duplicate the interface. Editable SVG icon assets are in `static/img/icons/`.

## 1. Run locally (Django website)
Python 3.11+ recommended.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000. Admin: http://127.0.0.1:8000/admin/

Windows PowerShell:
```powershell
Copy-Item .env.example .env
```

## 2. Run FastAPI separately
In another terminal, activate the same virtual environment:
```bash
uvicorn api.main:app --reload --port 8001
```
Open http://127.0.0.1:8001/docs for interactive API docs.
Set `PORTFOLIO_API_URL=http://127.0.0.1:8001` in `.env` if you want the frontend to use the API URL.

## 3. PostgreSQL
Set `DATABASE_URL` in `.env` to your PostgreSQL connection string, for example:
`postgresql://USER:PASSWORD@HOST:5432/DBNAME`
For local quick start, leave it empty and Django uses SQLite. For production, use Render's internal database URL and keep it secret.

### FastAPI web service
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`
- Environment variables:
  - `DATABASE_URL`: same Render PostgreSQL connection string
  - `CORS_ORIGINS`: `https://pravin-portfolio.onrender.com`
  - `API_ADMIN_TOKEN`: set a long random token if using protected API features

### After deploy
1. Run migrations using the Django build command above.
2. Open `/admin/` and create/update gallery items, project links, and profile details.
3. Test `/health/` on the FastAPI service and `/docs` for API documentation.
4. Configure persistent storage before enabling public user uploads in production.

## Security / production checklist
- Never commit `.env`, passwords, or secret keys.
- Set `DEBUG=False` on Render.
- Keep file upload size/type restrictions enabled; inspect uploaded files before public sharing.
- Contact form stores submissions in Django admin; add email delivery only after configuring SMTP.
- User comments are not publicly writable by default. Add moderation/authentication before enabling comments.
- `API_ADMIN_TOKEN` is a starter protection option, not a full user account system.
