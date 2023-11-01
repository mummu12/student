from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import StudentSerailizer
from crm.models import Students
from rest_framework.viewsets import ViewSet,ModelViewSet

class StudentView(APIView):
    def get(self,request,*args,**kwargs):
        # print("listing all records")
        # return Response(data={"massage":"listing student records"})
        qs=Students.objects.all()
        serializer=StudentSerailizer(qs,many=True) #deserialization
        return Response(data=serializer.data)
    
    
    def post(self,request,*args,**kwargs):
        # print("inserting student records")
        # return Response(data={"message":"created"})
        serializer=StudentSerailizer(data=request.data) #serialization
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    

class StudentDetailView(APIView):

    def get(self,request,*args,**kwargs):
        # print("student detail get method")
        # return Response(data={"message":"student detail"})
        id=kwargs.get("pk")
        qs=Students.objects.get(id=id)
        serializer=StudentSerailizer(qs)
        return Response(data=serializer.data)
        
    
    def put(self,request,*args,**kwargs):
        # print("student update method")
        # return Response(data={"message":"student changed"})
        id=kwargs.get("pk")
        obj=Students.objects.get(id=id)
        serializer=StudentSerailizer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Students.objects.filter(id=id).delete()
        return Response(data={"message":"student deleted"})
        
        # print("student delete method")
        # return Response(data={"message":"student deleted"})


class StudentViewSetView(ViewSet):
    
    def list(self,request,*args,**kwargs):
        qs=Students.objects.all()
        serializer=StudentSerailizer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Students.objects.get(id=id)
        serializer=StudentSerailizer(qs)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=StudentSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.erros)
        
        
        
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Students.objects.get(id=id)
        serializer=StudentSerailizer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.erros)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Students.objects.filter(id=id).delete()
        return Response(data={"message":"student deleted"})
        
        
class StudentModelViewSetView(ModelViewSet):
    serializer_class=StudentSerailizer
    queryset=Students.objects.all()
    
            

