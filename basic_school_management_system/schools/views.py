from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from .SchoolSerializer import *
from .models import *


class registerschool(APIView):
    def post(self, request):
        serializer = SchoolSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'satus':400,
                             'errors':serializer.errors,
                             'message':'Bad Request'})
        serializer.save()

        school_user = school.objects.get(email = serializer.data['email'])
        Refresh = RefreshToken.for_user(school_user)

        return Response({'status':200,
                         'payload':serializer.data,
                         'Refresh':str(Refresh),
                         'access':str(Refresh.access_token),
                         'message':'Your school is registered.'})


class AddStudent(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        students = request.data
        serializer = StudentSerializer(data = students)

        if not serializer.is_valid():
            return Response({'satus':400,
                             'errors':serializer.errors,
                             'message':'Bad Request'})
        
        serializer.save()
        return Response({
            'status':200,
            'payload':serializer.data,
            'message':'students are added'
        })

class UpdateStudent(APIView):

    def patch(self, request):
        try:
            student_obj = sutudent.objects.get(user_name=request.data['user_name'])
            serializer = StudentSerializer(student_obj, data= request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status':403,
                                 'error':serializer.errors,
                                 'message':'please try again.'})
            serializer.save()
            return Response({'status':200,
                             'payload':serializer.data,
                             'message':'data has been updated.'})
        
        except Exception as e:
            return Response({'status':403,
                             'message':'invalid user name or password'})
