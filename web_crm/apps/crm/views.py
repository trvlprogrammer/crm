from django.shortcuts import render

def crm_views(request):
    return render(request, "crm.html", {})
