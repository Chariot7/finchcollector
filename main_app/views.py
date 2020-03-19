from django.shortcuts import render
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'birdy', 'sqeeky squaker', 3),
  Finch('Sachi', 'green feathered', 'flies high', 0),
  Finch('Raven', 'midnight black', 'chirp chirp', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Finch peeps</h1>')
def about(request):
  return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})