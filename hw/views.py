from django.shortcuts import render

def html(request):
    return render(
        request=request,
        template_name="index.html")
