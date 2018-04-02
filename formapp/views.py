from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FormappForm
from .models import Inputs

n = 1


def formapp(request):
    global n
    forms = [FormappForm()] * n
    if request.method == 'POST':
        form = FormappForm(request.POST)
        if form.is_valid():
            input = Inputs(input_text=form.cleaned_data)
            input.save()
            n += 1
        return HttpResponseRedirect('/formapp/')
    else:
        a = 1
        for _ in forms:
            form = FormappForm(auto_id='id_for_%s', label_suffix=str(a))
            a += 1

    return render(request, 'formapp/formapp.html', {'forms': forms})


def inputs(request):
    inp = Inputs.objects.all()
    input = [i.input_text for i in inp]
    return render(request, 'formapp/inputs.html', {'input': input})
