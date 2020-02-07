from django.shortcuts import render

# define the definition/function to return our template page
def zinggrid(request):
    title = "My ZingGrid CRUD Example(s)"
    return render(request, 'zinggrid.html', {'title': title})