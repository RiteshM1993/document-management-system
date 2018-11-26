import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from docadmin.registeruser.registeruserservice.registeruserservice import docsUser
import time


@api_view(['POST'])
def saveUser(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    createdDate = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    docsUser_obj = docsUser()

    result = docsUser_obj.saveDocsUsers(username,email,password,createdDate)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def userCount(request):
    docsUser_obj = docsUser()

    result = docsUser_obj.DocsUserCount()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listUsers(request):
    docsUser_obj = docsUser()

    result = docsUser_obj.DocsUserList()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['DELETE'])
def deleteUser(request):
    id = request.GET['id']

    docsUser_obj = docsUser()

    result = docsUser_obj.DocsUserDelete(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getEditData(request):
    id = request.GET['id']

    docsUser_obj = docsUser()

    result = docsUser_obj.getEditUserData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['PUT'])
def updateUser(request):
    id = request.data['id']
    email = request.data['email']
    username = request.data['username']
    modifiedDate = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    docsUser_obj = docsUser()

    result = docsUser_obj.updateUserData(id, username, email,modifiedDate)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)