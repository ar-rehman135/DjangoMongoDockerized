from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Model Object - Single Std

def student_detail(request):
    stu = Student.objects.get(id = 1)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer.render(serializer.data)
    return render(json_data, content_type='application/json')