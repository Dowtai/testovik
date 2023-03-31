from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Test, Question, UserAnswer

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'option1', 'option2', 'option3', 'option4', 'correct_answer']
        labels = {
            'text': 'Вопрос',
            'option1': 'Вариант ответа 1',
            'option2': 'Вариант ответа 2',
            'option3': 'Вариант ответа 3',
            'option4': 'Вариант ответа 4',
            'correct_answer': 'Правильный ответ',
        }
        widgets = {
            'correct_answer': forms.RadioSelect(attrs={'class': 'radio'}),
        }

class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['user_answer']