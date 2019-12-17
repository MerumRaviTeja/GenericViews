from .models import *
from django.views.generic.edit import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect

class CompanyListView(ListView):
    model=Company
    fields="__all__"
class CompanyCreateView(CreateView):
    model=Company
    fields="__all__"
    success_url=reverse_lazy('companies')
class CompanyDetailView(DetailView):
    model=Company
    fields="__all__"
class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo')
class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')


def show_view(request):
        employees=Employee.objects.all()

        if employees:
              return redirect('/')
        else:
            return render(request,'sample1/index.html',{'employees':employees})
  




















# # from sample1.forms import *
# # from django.shortcuts import redirect,render 
# # def emp(request):  
# #     if request.method == "POST":  
# #         form = EmployeeForm(request.POST)  
# #         if form.is_valid():  
# #             try:  
# #                 return redirect('/')  
# #             except:  
# #                 pass  
# #     else:  
# #         form = EmployeeForm()  
# #     return render(request,'sample1/signup.html',{'form':form}) 

# from .models import Post 
# from .forms import PostForm 
# from .import views 
# from django.shortcuts import HttpResponse, render, redirect 
# def cart_home(request):
#     print(request.session)
#     print(dir(request.session))
#     request.session.set_expiry(0)
#     # k=request.session.session_key
#     # print(k)
#     return render(request,"sample1/home.html",{})

# def home(request): 
  
#     # check if the request is post  
#     if request.method =='POST':   
  
#         # Pass the form data to the form class 
#         details = PostForm(request.POST) 
  
#         # In the 'form' class the clean function  
#         # is defined, if all the data is correct  
#         # as per the clean function, it returns true 
#         if details.is_valid():   
  
#             # Temporarily make an object to be add some 
#             # logic into the data if there is such a need 
#             # before writing to the database    
#             post = details.save(commit = False) 
  
#             # Finally write the changes into database 
#             post.save()   
  
#             # redirect it to some another page indicating data 
#             # was inserted successfully 
        
#             return HttpResponse("OK") 
              
#         else: 
          
#             # Redirect back to the same page if the data 
#             # was invalid 
#             return render(request, "sample1/signup.html", {'form':details})   
#     else: 
  
#         # If the request is a GET request then, 
#         # create an empty form object and  
#         # render it into the page 
#         form = PostForm(None)    
#         return render(request, 'sample1/signup.html', {'form':form}) 
# from django.core.mail import EmailMessage
# from django.http import HttpResponse

# def sendEmailWithAttach(request):
#    html_content = "Comment tu vas?"
#    email = EmailMessage("my subject", html_content, "gamerboy456456@gmail.com", ["gamerboy456456@gmail.com"])
#    email.content_subtype = "html"
   
#    fd = open('/home/pnv/sample/sample1/tests.py', 'r')
#    email.attach('/home/pnv/sample/sample1/tests.py', fd.read(), 'text/plain')
   
#    res = email.send()
#    return HttpResponse('%s'%res)
# # from django.core.mail import EmailMessage
# # from django.http import HttpResponse

# # def sendHTMLEmail(request):
# #    html_content = "<strong>Comment tu vas?</strong>"
# #    email = EmailMessage("my subject", html_content, "gamerboy456456@gmail.com", ["gamerboy456456@gmail.com"])
# #    email.content_subtype = "html"
# #    res = email.send()
# #    return HttpResponse('%s'%res)
# # def gmail(request):
# #     from django.core.mail import send_mass_mail
# #     from django.http import HttpResponse


# #     msg1 = ('subject 1', 'message 1', "gamerboy456456@gmail.com", ["gamerboy456456@gmail.com"])
# #     msg2 = ('subject 2', 'message 2', "gamerboy456456@gmail.com", ["gamerboy456456@gmail.com"])
# #     res = send_mass_mail((msg1, msg2), fail_silently = False)
# #     return HttpResponse('%s'%res)
#     # from django.core.mail import send_mail
#     # send_mail('test email', 'hello world', "gamerboy456456@gmail.com", ["gamerboy456456@gmail.com"])
#     # from django.core.mail import get_connection, EmailMultiAlternatives

#     # connection = get_connection() # uses SMTP server specified in settings.py
#     # connection.open() # If you don't open the connection manually, Django will automatically open, then tear down the connection in msg.send()

#     # # html_content = render_to_string('newsletter.html', {'newsletter': n,})               
#     # text_content = "..."                      
#     # msg = EmailMultiAlternatives("subject", text_content, "gamerboy456456@gmail.com", ["gamerboy456456@gmail.com"],bcc=['raviteja87731@gmail.com','srikarp1995@gmail.com',], connection=connection)                                      
#     # # msg.attach_alternative(html_content, "text/html")                                                                                                                                                                               
#     # msg.send() 
#     # #Use 'bcc' e.g.: msg = EmailMultiAlternatives("subject", text_content, "from@bla", ["to@bla"], bcc=["to2@bla", "to3@bla"], connection=connection)

#     # connection.close() # Cleanup

#     # email = EmailMessage('Subject', 'Body', to=['gamerboy456456@gmail.com'])
#     # email.send()
#     # return HttpResponse("Ok")