



from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Faculty
from service.forms import FacultyForm
from service.service.FacultyService import FacultyService


from django.http.response import JsonResponse
import json
from django.core import serializers   

class FacultyCtl(BaseCtl): 
    
    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form["firstName"] = requestForm["firstName"]
        self.form["lastName"] = requestForm["lastName"]
        self.form["email"] = requestForm["email"]
        self.form["password"] = requestForm["password"]
        self.form["address"] = requestForm["address"]
        self.form["gender"] = requestForm["gender"]
        self.form["dob"] = requestForm["dob"]
        self.form["college_ID"] = requestForm["college_ID"]
        self.form["subject_ID"] = requestForm["subject_ID"]
        self.form["course_ID"] = requestForm["course_ID"]
        

    def get(self,request, params = {}):
        service=FacultyService()
        c=service.get(params["id"])
        res={}
        if(c!=None):
            res["data"]=c.to_json()
            res["error"]=False
            res["message"]="Data is found"
        else:
            res["error"]=True
            res["message"]="record not found"
        return JsonResponse({"data":res["data"]})

    def delete(self,request, params = {}):
        service=FacultyService()
        c=service.get(params["id"])
        res={}
        if(c!=None):
            service.delete(params["id"])
            res["data"]=c.to_json()
            res["error"]=False
            res["message"]="Data is Successfully deleted"
        else:
            res["error"]=True
            res["message"]="Data is not deleted"
        return JsonResponse({"data":res})


   



   

    def search(self,request, params = {}):
        json_request=json.loads(request.body)
        if(json_request):
            params["collegeName"]=json_request.get("collegeName",None)
            params["courseName"]=json_request.get("courseName",None)
        service=FacultyService()
        c=service.search(params)
        res={}
        data=[]
        for x in c:
            data.append(x.to_json())
        if(c!=None):
            res["data"]=data
            res["error"]=False
            res["message"]="Data is found"
        else:
            res["error"]=True
            res["message"]="record not found"
        return JsonResponse({"data":res})



    def form_to_model(self,obj,request):
        pk = int(request["id"])
        if(pk>0):
            obj.id = pk
        obj.firstName = request["firstName"]
        obj.lastName = request["lastName"]
        obj.email=request["email"] 
        obj.password=request["password"] 
        obj.address=request["address"]  
        obj.gender=request["gender"]  
        obj.dob=request["dob"]  
        obj.college_ID=request["college_ID"]  
        obj.subject_ID=request["subject_ID"]  
        obj.course_ID=request["course_ID"]  
       
        return obj

    def save(self,request, params = {}):      
        json_request=json.loads(request.body)
        self.request_to_form(json_request)
        res={}
        if(self.input_validation()):
            res["error"]=True
            res["message"]="Data is not saved"
        else:
            r=self.form_to_model(Faculty(), json_request)
            service=FacultyService()
            c=service.save(r)
            
            if(r!=None):
                res["data"]=r.to_json()
                res["error"]=False
                res["message"]="Data is Successfully saved"    
        return JsonResponse({"data":res,'form':self.form})

    def input_validation(self):
        inputError = self.form["inputError"]
        if (DataValidator.isNull(self.form["firstName"])):
            inputError["firstName"] = "Name can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["lastName"])):
            inputError["lastName"] = "last name can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["email"])):
            inputError["email"] = "email can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["password"])):
            inputError["password"] = "password can not be null"
            self.form["error"] = True
        
        if (DataValidator.isNull(self.form["address"])):
            inputError["address"] = "Address can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["gender"])):
            inputError["gender"] = "gender can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["dob"])):
            inputError["dob"] = "dob can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["college_ID"])):
            inputError["college_ID"] = "college_ID can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["subject_ID"])):
            inputError["subject_ID"] = "subject_ID can not be null"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["course_ID"])):
            inputError["course_ID"] = "course_ID can not be null"
            self.form["error"] = True                  
        return self.form["error"]

    # Template html of Role page    
    def get_template(self):
        return "orsapi/AddFaculty.html"          

    # Service of Role     
    def get_service(self):
        return FacultyService()        
