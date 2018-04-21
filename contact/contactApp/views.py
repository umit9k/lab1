from .models import Contact
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm

# Create your views here.
def contact_list(request):
	contacts = Contact.objects.all()
	return render(request, 'contact/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/contact_detail.html', {'contact': contact})

def contact_new(request):
    if request.method == "CONTACT":
        form = ContactForm(request.CONTACT)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contact/contact_edit.html', {'form': form})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "CONTACT":
        form = ContactForm(request.CONTACT, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/contact_edit.html', {'form': form})