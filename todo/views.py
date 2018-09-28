from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.


""" def hello(request):
	return HttpResponse("Hello World") """

""" def todo_list(request):
	return render(request, "todo_list.html") """

	

# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {
        'items': results
    })


def create_an_item(request):
    if request.method == "POST":		
        form = ItemForm(request.POST, request.FILES)
        new_item = Item()
        if form.is_valid():
        	form.save()
        return redirect(get_todo_list)

        # new_item.name = request.POST.get('name')
        # new_item.done = 'done' in request.POST
        # new_item.save()

    else:
    	form = ItemForm()
    return render(request, "form.html", {
        'form': form
    })


def edit_an_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)
    return render(request, "form.html", {'form': form})


def toggle(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)
	
