# from django.shortcuts import render

# from django.http import JsonResponse

from students.models import Student
from employees.models import Employee
from .serializers import SerializerStudent, SerializerEmployee
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets

from blogs.models import Blog, Comment
from blogs.serializers import SerializerBlog, SerializerComment
# Create your views here.

@api_view(['GET','POST'])
def studentView(request):
    if request.method=='GET':
        student=Student.objects.all()
        serializer=SerializerStudent(student, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=SerializerStudent(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=SerializerStudent(student)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    elif request.method=='PUT':
        serializer=SerializerStudent(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



# class Employees(APIView):
#     def get(self,request):
#         employee=Employee.objects.all()
#         serializer=SerializerEmployee(employee,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer=SerializerEmployee(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error, status.HTTP_400_BAD_REQUEST)


# class EmployeesDetails(APIView):

#     def get_emp(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         employee=self.get_emp(pk)
#         serializer=SerializerEmployee(employee)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def delete(self, request, pk):
#         emp=self.get_emp(pk)
#         emp.delete()
#         return Response(status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         emp=self.get_emp(pk)
#         serializer=SerializerEmployee(emp, request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

'''
# mixins
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmployee

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class EmployeesDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmployee

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

'''
# generics
class Employees(generics.ListAPIView, generics.CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmployee


class EmployeesDetails(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmployee
    lookup_fiel='pk'
'''

# model view set

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmployee


class BlogsView(generics.ListAPIView, generics.CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=SerializerBlog

class BlogsDetails(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=SerializerBlog
    look_up_fields='pk'

class CommentView(generics.ListAPIView, generics.CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=SerializerComment

class CommentsDetails(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=SerializerComment
    look_up_fields='pk'