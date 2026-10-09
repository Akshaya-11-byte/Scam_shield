from django.shortcuts import render

def home(request):
    message = ""

    if request.method == "POST":
        message = request.POST.get("message", "")

    return render(request, "detector/home.html", {
        "message": message
    })
