from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
@api_view(['GET'])
def home(request):
    data = Student.objects.all()
    serializer = StudentSerializer(data, many=True)
    return Response({'data': serializer.data})

@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({'status': 403, 'errors': serializer.errors})
    
    serializer.save()
    
    return Response({'status': 200, 'payload': serializer.data, 'message': 'Data Saved'})
