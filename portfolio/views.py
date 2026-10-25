import os
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import GalleryItem, ContactMessage

PROFILE = {
    "name": "Pravin Dayanand Bansode",
    "role": "Python Developer",
    "location": "Pune, Maharashtra",
    "email": "pravinbansode147@gmail.com",
    "phone": "7666656710",
    "linkedin": "https://linkedin.com/in/pravin-bansode",
    "summary": "Python Developer with hands-on experience building web applications and REST APIs using Django, Django REST Framework and Flask, backed by PostgreSQL and MySQL.",
    "skills": {
        "Languages": ["Python", "SQL", "JavaScript", "HTML5", "CSS3", "JSON"],
        "Frameworks": ["Django", "Django REST Framework", "Flask", "Pandas", "NumPy", "Requests"],
        "Databases": ["PostgreSQL", "MySQL", "Schema design", "Indexing", "Query optimization"],
        "Tools": ["Git", "GitHub", "Postman", "Render", "VS Code"],
        "Concepts": ["RESTful API design", "Authentication", "CRUD", "MVT architecture", "Debugging"],
        "Data & BI": ["Power BI", "Microsoft Excel"],
    },
    "experience": [
        {"role":"Python Developer", "company":"Microdynamics Software Solutions Pvt Ltd", "dates":"April 2026 – Present", "items":["Build and maintain full-stack web applications using Python, Django and Flask.","Design and deploy REST APIs with Django REST Framework.","Design PostgreSQL and MySQL schemas and write complex SQL queries.","Debug issues using server logs and error-tracking tools."]},
        {"role":"Sales Executive, Analysis & Business Development", "company":"Infinity Retail Limited", "dates":"Jan 2025 – Apr 2026", "items":["Analysed store-level sales, walk-in and ticket data across categories, supporting revenue tracking of about INR 4 Cr.","Built employee performance dashboards and MTD sales reports.","Consolidated sales, operations and customer data into structured reports."]},
        {"role":"Backend Support SQL Developer", "company":"Wapmebs Global Services Pvt Ltd, Pune", "dates":"Aug 2023 – Oct 2024", "items":["Wrote SQL queries with multi-table joins, subqueries and aggregations.","Cleaned and validated data and maintained relational databases.","Optimized queries and added basic indexing."]},
    ],
    "projects": [
        {"name":"Pics — Imitation Jewellery E-Commerce", "stack":"Django · DRF · PostgreSQL · JavaScript · Render", "description":"Deployed full-stack e-commerce app with product catalogue, cart and shop pages; DRF JSON endpoints support product filtering, categories and inventory updates."},
        {"name":"LWT — Learn With Tech", "stack":"Django · DRF · PostgreSQL · HTML/CSS · JavaScript", "description":"Community learning platform to learn, teach and share resources, with video tutorials, downloadable study material and career learning roadmaps."},
        {"name":"VBI — Virtual Bank of India (Demo)", "stack":"Django · PostgreSQL · HTML/CSS · JavaScript", "description":"Demo banking application with authentication, balance tracking, deposits and fund transfers; uses .env configuration and PostgreSQL transaction records."},
        {"name":"Pravin Bansode Portfolio", "stack":"Django · Neon PostgreSQL · Git+GitHub · Vercel", "description":"Personal developer portfolio website built with Django and Neon PostgreSQL, featuring dynamic content management, secure environment configurations, and optimized pre-deployment asset handling."},
    ],
    "education": "BCA — Bharati Vidyapeeth Deemed to be University, Pune (Sangli), 2020–2023 · CGPA 8.54/10",
    "certifications": ["Deloitte — Data Analytics Job Simulation (Forage)", "Accenture — Data Analytics and Visualization Job Simulation (Forage)"],
}

def home(request):
    items = GalleryItem.objects.filter(is_public=True).order_by("-created_at")[:12]
    return render(request, "portfolio/home.html", {"profile": PROFILE, "gallery_items": items})

def gallery(request):
    items = GalleryItem.objects.filter(is_public=True).order_by("-created_at")
    return render(request, "portfolio/gallery.html", {"items": items, "profile": PROFILE})

@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
        if not (name and email and message):
            messages.error(request, "Please fill in your name, email and message.")
            return redirect("/#contact")
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Thanks! Your message has been saved.")
        return redirect("/#contact")
    return redirect("/#contact")

def health(request):
    return JsonResponse({"status":"ok", "service":"Django portfolio"})
