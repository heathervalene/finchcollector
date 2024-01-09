from django.shortcuts import render


finches = [
  {'name': 'Crested bunting', 'distribution': 'Southeast Asia', 'habitat': 'subtropic', 'color': 'black and red', 'description': 'little jerk'},
  {'name': 'Yellowhammer', 'distribution': 'Europe', 'habitat': 'dry, open country', 'color': 'yellow', 'description': 'annoying AF'},
]



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })