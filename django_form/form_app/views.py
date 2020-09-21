from django.contrib import messages
from django.shortcuts import render

from .forms import EntrepreneurForm


def index(request):
    if request.method == 'POST':
        form = EntrepreneurForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Submission was successful')
            return render(request, 'index.html', context={'form': EntrepreneurForm()})
        else:
            print('----> form errors: ', form.errors)
    else:
        form = EntrepreneurForm()
    return render(request, 'index.html', context={'form': form})
