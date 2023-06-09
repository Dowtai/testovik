from django.db import models
from django.conf import settings
from django.utils import timezone

class Test(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correct_answer = models.PositiveIntegerField(choices=((1, 'Ответ 1'), (2, 'Ответ 2'), (3, 'Ответ 3'), (4, 'Ответ 4')), blank=True, null=True)

    def __str__(self):
        return self.text

class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='results')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    user_answers = []

    def __str__(self):
        return self.user.username + ' решил(а) ' + self.test.title
    
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='qanswers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_answer = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, ' 4')))
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name='tanswers')

    def __str__(self):
        return self.user.username + ' ответил(а) на ' + self.question.text
