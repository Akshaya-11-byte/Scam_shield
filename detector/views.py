from django.shortcuts import render


def home(request):
    message = ""
    warnings = []
    recommendations = []
    risk_level = "Low"

    if request.method == "POST":
        message = request.POST.get("message", "").strip()
        text = message.lower()

        # 1. Prize and lottery scams
        if any(word in text for word in ["won", "prize", "lottery"]):
            warnings.append(
                "Prize or lottery claims may be used to trick people."
            )
            recommendations.append(
                "Do not pay a fee to claim an unexpected prize. "
                "Verify the claim independently."
            )

        # 2. OTP and account security
        if "otp" in text or "one-time password" in text:
            warnings.append(
                "Never share an OTP or one-time password with anyone."
            )
            recommendations.append(
                "Never share your OTP. If you did not request it, "
                "secure your account and contact the official provider."
            )

        # 3. Job-related payments
        if (
            "registration fee" in text
            or "pay to get a job" in text
            or "job fee" in text
        ):
            warnings.append(
                "A job offer demanding upfront payment may be suspicious."
            )
            recommendations.append(
                "Verify the employer through its official website "
                "and recruitment contact before paying any fee."
            )

        # 4. Urgent payment demands
        if (
            "urgent payment" in text
            or "pay immediately" in text
            or "account will be blocked" in text
        ):
            warnings.append(
                "Urgent payment or account-threat messages can be pressure tactics."
            )
            recommendations.append(
                "Do not rush into payment. Contact the organization "
                "through a verified phone number or official website."
            )

        # 5. Bank and personal information
        if (
            "bank details" in text
            or "card number" in text
            or "cvv" in text
            or "password" in text
        ):
            warnings.append(
                "The message mentions sensitive financial or login information."
            )
            recommendations.append(
                "Do not share passwords, CVV numbers, or banking details "
                "through an unverified message."
            )

        # 6. Suspicious link language
        if (
            "click this link" in text
            or "verify your account" in text
            or "claim your reward" in text
        ):
            warnings.append(
                "Unexpected links and account-verification requests "
                "should be checked carefully."
            )
            recommendations.append(
                "Avoid opening unexpected links. Visit the official website "
                "directly instead."
            )

        # 7. Suspicious job offers
        if (
            "work from home" in text
            or "earn money daily" in text
            or "guaranteed income" in text
            or "no interview" in text
        ):
            warnings.append(
                "Unrealistic income promises or unusual hiring claims "
                "may indicate a suspicious job offer."
            )
            recommendations.append(
                "Check the employer, job description, and recruiter identity. "
                "Be cautious of guaranteed earnings and requests for money."
            )

        # 8. Phishing and account impersonation
        if (
            "verify immediately" in text
            or "suspended account" in text
            or "confirm your identity" in text
            or "update your kyc" in text
        ):
            warnings.append(
                "Unexpected account-verification or KYC requests "
                "may be phishing attempts."
            )
            recommendations.append(
                "Check account alerts directly in the official app or website. "
                "Do not use verification links from unexpected messages."
            )

        # 9. Suspicious app installation
        if (
            "install this app" in text
            or "download this apk" in text
            or "install apk" in text
        ):
            warnings.append(
                "Requests to install apps from unknown sources may be risky."
            )
            recommendations.append(
                "Do not install APK files from untrusted links. "
                "Use official app stores or the developer's verified website."
            )

        # 10. Determine illustrative risk level
        if len(warnings) == 0:
            risk_level = "Low"
        elif len(warnings) == 1:
            risk_level = "Medium"
        else:
            risk_level = "High"

        # 11. Provide general advice when no rules match
        if not warnings:
            recommendations.append(
                "No warning signs matched the current rules. "
                "This does not guarantee that the message is safe. "
                "Verify unexpected requests independently."
            )

        # Remove duplicate recommendations
        recommendations = list(dict.fromkeys(recommendations))

    # 12. Send results to the HTML page
    return render(
        request,
        "detector/home.html",
        {
            "message": message,
            "warnings": warnings,
            "recommendations": recommendations,
            "risk_level": risk_level,
        },
    )
