
import json
import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Registration


@csrf_exempt
def register_student(request):
    if request.method != "POST":
        return JsonResponse(
            {"success": False, "message": "POST method required."},
            status=405,
        )

    try:
        data = json.loads(request.body)

        name = str(data.get("name", "")).strip()
        email = str(data.get("email", "")).strip().lower()
        phone = str(data.get("phone", "")).strip()
        college = str(data.get("college", "")).strip()
        branch = str(data.get("branch", "")).strip()
        year = str(data.get("year", "")).strip()
        event_name = str(data.get("event", "")).strip()

        if not all([
            name, email, phone, college,
            branch, year, event_name
        ]):
            return JsonResponse(
                {"success": False, "message": "Please fill all fields."},
                status=400,
            )

        if len(name) > 150 or len(college) > 200:
            return JsonResponse(
                {"success": False, "message": "One or more fields are too long."},
                status=400,
            )

        if len(branch) > 100 or len(event_name) > 100:
            return JsonResponse(
                {"success": False, "message": "Invalid branch or event name."},
                status=400,
            )

        if len(phone) > 20 or not re.fullmatch(r"[0-9+\-\s()]{7,20}", phone):
            return JsonResponse(
                {"success": False, "message": "Enter a valid phone number."},
                status=400,
            )

        if len(email) > 254 or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+", email
        ):
            return JsonResponse(
                {"success": False, "message": "Enter a valid email address."},
                status=400,
            )

        allowed_years = {
            "1st Year", "2nd Year", "3rd Year", "4th Year"
        }
        allowed_events = {
            "Hackathon", "AI Workshop", "Web Design",
            "Coding Contest", "Robotics", "Tech Quiz"
        }

        if year not in allowed_years or event_name not in allowed_events:
            return JsonResponse(
                {"success": False, "message": "Select a valid year and event."},
                status=400,
            )

        if Registration.objects.filter(
            email=email, event_name=event_name
        ).exists():
            return JsonResponse(
                {
                    "success": False,
                    "message": "This email is already registered for this event."
                },
                status=409,
            )

        Registration.objects.create(
            student_name=name,
            email=email,
            phone=phone,
            college=college,
            branch=branch,
            year=year,
            event_name=event_name,
        )

        return JsonResponse(
            {
                "success": True,
                "message": "Registration saved successfully!"
            },
            status=201,
        )

    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"success": False, "message": "Invalid request data."},
            status=400,
        )
