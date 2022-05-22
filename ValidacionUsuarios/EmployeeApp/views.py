from email.policy import default
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http.response import JsonResponse
from  EmployeeApp.models import  Nombres
from  EmployeeApp.serializers import  NombresSerializer
 

# Create your views here.
@csrf_exempt
def  nombreApi(request,id=1):
    if request.method=='GET':
        nombres=Nombres.objects.all()
        nombres_serializer=NombresSerializer(nombres,many=True)
        return JsonResponse(nombres_serializer.data,safe=False)
    elif  request.method=='POST':
           nombres_data=JSONParser().parse(request)
           nombres_serializer=NombresSerializer(data=nombres_data)
    if nombres_serializer.is_valid():#utilizamos el serializador para validar el modelo
        nombres_serializer.save()# si es  valido se guarda la informacion  en BD
    return JsonResponse("Nombres registrados correctamente",safe=False)
    if  request.method=='POST':
           nombres_data=JSONParser().parse(request)
           nombres_serializer=NombresSerializer(data=nombres_data)
    if nombres_serializer.is_invalid():#utilizamos el serializador para validar el modelo
        print("los datos no son validos")
    return JsonResponse("no se encontraron resultados",safe=True)


  #  (nombreApi==0):
       # return  JsonResponse("Los datos  no son invalidos",safe=True)

   # elif request.method=='POST':
      #  nombres_data=JSONParser().parse(request)
     #   nombres_serializer=NombresSerializer(data=nombres_data)
      #if nombres_serializer.is_invalid():#utilizamos el serializador para validar el modelo
      #  nombres_serializer.save()# si es  valido se guarda la informacion  en BD
    # return JsonResponse("Datos no encontrados",safe=False)