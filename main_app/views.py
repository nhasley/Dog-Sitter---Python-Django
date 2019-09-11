from django.shortcuts import render

from django.http import HttpResponse

class Dog:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Norman', 'dalmation', 'Active', 3),
  Dog('David', 'husky', 'Good at Fetch', 0),
  Dog('Bobbi', 'corgi', 'Fluffy dog', 4)
]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
def about(request):
  return render(request, 'about.html')
def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })