from django import forms
from django.forms import Form,ModelForm
from . models import Book,Student
from django.contrib.auth.models import User
from . import models


class BookUpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = ('cover','name','author','isbn','category')
        
        widgets={
            'cover': forms.FileInput(attrs={'class':'form-control w-50'}),
            'name': forms.TextInput(attrs={'class':'form-control w-50'}),
            'author': forms.TextInput(attrs={'class':'form-control w-50'}),
            'isbn': forms.TextInput(attrs={'class':'form-control w-50'}),
            'category': forms.TextInput(attrs={'class':'form-control w-50'}),
            
        }
     
     
class IssueBookForm(forms.Form):
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Book Name [ISBN]", to_field_name="isbn", label="Book (Name and ISBN)")
    name2 = forms.ModelChoiceField(queryset=models.Student.objects.all(), empty_label="Name [Branch] [Class] [Roll No]", to_field_name="user", label="Student Details")
    
    isbn2.widget.attrs.update({'class': 'form-control'})
    name2.widget.attrs.update({'class':'form-control'})
   
       
        
        
        
class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ('user','classroom','branch','roll_no','phone','image')
        
        widgets={
            'user':forms.TextInput(attrs={'class':'form-control w-50'}),
            'classroom':forms.TextInput(attrs={'class':'form-control w-50'}),
            'branch':forms.TextInput(attrs={'class':'form-control w-50'}),
            'roll_no':forms.TextInput(attrs={'class':'form-control w-50'}),
            'phone':forms.TextInput(attrs={'class':'form-control w-50'}),
            'image': forms.FileInput(attrs={'class':'form-control w-50'}),
            
            
        }
    



