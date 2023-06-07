from django.shortcuts import render,redirect
from .models import Message
from .forms import SendMessageForm

# Create your views here.
def send_message(request):
    if request.method == "GET":
        form = SendMessageForm()
        return render(request,'send_message.html',{'form':form})
    else:
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/messagingapp/messages')

def show_messages(request, pk):
    if request.method == "GET":
        messages = Message.objects.all()
        return render(request,'messages.html',{'messages':messages})
    else: 
        reply_to_message(request,pk)
    
def reply_to_message(request, pk):
    message = Message.objects.get(pk=pk)
    return render(request,'reply.html',{'message':message})