from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from home.serializers import PeopleSerializer


@api_view(['GET', 'POST'])
def index(request):
    course = {
        "course_name":"Pyhton",
        "learn":['flask', 'django', 'fastAPI'],
        "courseProvider":"Scalar"
    }
    if request.method =='GET':
        return Response(course)
    elif request.method =='POST':
        return Response(course)
    

@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializers = PeopleSerializer(objs, many = True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = request.data
        serializers = PeopleSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id = data["id"])
        serializers = PeopleSerializer(obj, data=data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    elif request.method == "PUT":
        data = request.data
        obj = Person.objects.get(id = data["id"])
        serializers = PeopleSerializer(obj, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    elif request.method == "DELETE":
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({"message":"Person has been deleted successfully"})