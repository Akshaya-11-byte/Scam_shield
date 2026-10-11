
from django.shortcuts import render


def home(request):
    message = ""
    warnings = []
    risk_level = "Low"

    if request.method == "POST":
        message = request.POST.get("message", "").strip()
        text = message.lower()

        # Prize and reward warning signs
        if "won" in text or "prize" in text or "lottery" in text:
            warnings.append(
                "Prize or lottery claims may be used to trick people."
            )

        # OTP and account security
        if "otp" in text or "one-time password" in text:
            warnings.append(
                "Never share an OTP or one-time password with anyone."
            )

        # Job-related payments
        if (
            "registration fee" in text
            or "pay to get a job" in text
            or "job fee" in text
        ):
            warnings.append(
                "A job offer demanding upfront payment may be suspicious."
            )

        # Urgent payment demands
        if (
            "urgent payment" in text
            or "pay immediately" in text
            or "account will be blocked" in text
        ):
            warnings.append(
                "Urgent payment or account-threat messages can be pressure tactics."
            )

        # Bank and personal information
        if (
            "bank details" in text
            or "card number" in text
            or "cvv" in text
            or "password" in text
        ):
            warnings.append(
                "Be careful when a message asks for sensitive financial or login information."
            )

        # Suspicious link language
        if (
            "click this link" in text
            or "verify your account" in text
            or "claim your reward" in text
        ):
            warnings.append(
                "Unexpected links and account-verification requests should be checked carefully."
            )

        # Simple illustrative risk categories
        if len(warnings) == 0:
            risk_level = "Low"
        elif len(warnings) == 1:
            risk_level = "Medium"
        else:
            risk_level = "High"

    return render(request, "detector/home.html", {
        "message": message,
        "warnings": warnings,
        "risk_level": risk_level,
    })
