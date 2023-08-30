from django.shortcuts import render

def sales_views(request):
    return render(request, "sales.html", {})
