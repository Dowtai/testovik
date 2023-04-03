from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Test, Question, UserAnswer, TestResult
from .forms import CustomUserCreationForm, TestForm, QuestionForm, UserAnswerForm
from django.forms import formset_factory, modelformset_factory
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_or_register(request):
    return render(request, 'login_or_register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    tests = Test.objects.all()
    return render(request, 'home.html', {'tests': tests})

@login_required
def create_test(request):
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        if test_form.is_valid():
            test = test_form.save(commit=False)
            test.author = request.user
            test.save()
            messages.success(request, 'Test created successfully.')
            return redirect('add_questions', test_id=test.pk)
    else:
        test_form = TestForm()
    return render(request, 'create_test.html', {'test_form': test_form})

@login_required
def test_delete(request, test_id):
    test = get_object_or_404(Test, pk=test_id, author=request.user)
    if request.method == 'POST':
        test.delete()
        messages.success(request, 'Test deleted successfully.')
        return redirect('home')
    return render(request, 'test_delete.html', {'test': test})

@login_required
def add_questions(request, test_id):
    test = get_object_or_404(Test, pk=test_id, author=request.user)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.test = test
            question.save()
            messages.success(request, 'Question added successfully.')
            return redirect('add_questions', test_id=test.pk)
    else:
        question_form = QuestionForm()

    return render(request, 'add_questions.html', {'test': test, 'question_form': question_form})

@login_required
def solve_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = test.questions.all()
    if request.method == 'POST':
        user_answers = []
        test_result = TestResult(test=test, user=request.user)
        test_result.save()
        for x in range(1, len(questions) + 1):
            User_Answer = UserAnswer(question=questions[x - 1], user=request.user, user_answer=request.POST.get('user_answer_' + str(x)), test_result=test_result)
            User_Answer.save()
            user_answers.append(User_Answer)
            
        return redirect('result', result_id=test_result.pk)
    else:
        formset = []
        for question in questions:
            formset.append([question, UserAnswerForm()])
    return render(request, 'solve_test.html', {'user': request.user, 'test': test, 'formset': formset})

@login_required
def test_details(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    test_form = TestForm(test)
    return render(request, 'test_details.html', {'test': test_form})

@login_required
def test_results(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    results = test.results.all()
    return render(request, 'test_results.html', {'test': test, 'results': results})

@login_required
def result(request, result_id):
    result = get_object_or_404(TestResult, pk=result_id)
    allq = 0
    goodq = 0
    for answer in result.tanswers.all():
        if answer.question.correct_answer != None:
            allq += 1
            if answer.user_answer == answer.question.correct_answer:
                goodq += 1
    if (allq == 0):
        percentage = round(100, 2)
    else:
        percentage = round(goodq/allq * 100, 2)
    return render(request, 'result.html', {'result': result, 'goodq': goodq, 'allq': allq, 'percentage': percentage, 'ruser': request.user})
