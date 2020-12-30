from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.models import User
from service.forms import UserForm
from service.service.UserService import UserService


from django.http.response import JsonResponse
import json
from django.core import serializers

class LoginCtl(BaseCtl):
    def request_to_form(self, requestForm):
        self.form["login_id"] = requestForm["login_id"]
        self.form["password"] = requestForm["password"]
        

    def form_to_model(self,obj,request):
        obj.login_id = request["login_id"]
        obj.password = request["password"]
        return obj
    
    def auth(self,json_request):
        q = User.objects.filter()
        if(json_request.get("login_id")!=None ):
            q= q.filter( login_id = json_request.get("login_id"))  
        if(json_request.get("password")!=None ):
            q= q.filter( password = json_request.get("password"))
        userList = q
        if (userList.count() > 0):
            for userData in userList:
                print(json_request.get("login_id")==userData.login_id)
               
                if(json_request.get("login_id")==userData.login_id):
                    return userData
        else:
            
            return None
        
    def save(self,request, params = {}):  
        json_request=json.loads(request.body)
        user=self.auth(json_request)    
        res={}                
        if(user is None):
            self.form["error"] = True
            self.form["message"] = "Invalid ID or Password"
            res = JsonResponse({"data":res,'form':self.form}) 
           
        else:
            request.session["user"] = user
            self.form["message"] = "LogIn Sucessful"
            self.form["error"] = False
            res = JsonResponse({"data":res,'form':self.form})     
        return res

    def input_validation(self):
        inputError = self.form["inputError"]
        if (DataValidator.isNull(self.form["login_id"])):
            inputError["login_id"] = "login_id can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["password"])):
            inputError["password"] = "password can not be null"
            self.form["error"] = True
       
        return self.form["error"]

    # Template html of Role page    
    def get_template(self):
        return "orsapi/Login.html"          

    # Service of Role     
    def get_service(self):
        return UserService()        