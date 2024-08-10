from django.shortcuts import render, HttpResponse

html_base = """
<h1>Hello World</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portfolio">Portafolio</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")


def contac(request):
    return render(request, "core/contac.html")


