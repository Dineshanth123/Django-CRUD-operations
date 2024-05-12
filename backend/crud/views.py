from django.shortcuts import render
from .models import Courses
from .serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({"Courses": serializer.data})

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def course_detail(request,id):
    
    course=Courses.objects.get(pk=id)
    
    if request.method=='GET':
        if request.method == 'GET':
            serializer = CourseSerializer(course)
            return Response({"Courses": serializer.data})
        
    elif request.method=='PUT':
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    