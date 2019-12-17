# # from django import forms  
# # from sample1.models import Employee  
  
# # class EmployeeForm(forms.ModelForm):  
# #     class Meta:  
# #         model = Employee  
# #         fields = "__all__"
# from django.forms import ModelForm 
# from django import forms 
  
# # define the class of a form 
# from sample1.models import *
# class PostForm(ModelForm): 
#     class Meta:
#         # write the name of models for which the form is made 
#         model = Post         
  
#         # Custom fields 
#         fields =["username", "gender", "text"] 
  
#     # this function will be used for the validation 
#     def clean(self): 
  
#         # data from the form is fetched using super function 
#         super(PostForm, self).clean() 
          
#         # extract the username and text field from the data 
#         username = self.cleaned_data.get('username') 
#         text = self.cleaned_data.get('text') 
  
#         # conditions to be met for the username length 
#         if len(username) < 5: 
#             # self._errors['username'] = self.error_class([ 
#             #     'Minimum 5 characters required']) 
#             self._errors['username']=self.error_class(['Mininmum 5'])
#         if len(text) <10: 
#             self._errors['text'] = self.error_class([ 
#                 'Post Should Contain minimum 10 characters']) 
  
#         # return any errors if found 
#         return self.cleaned_data 