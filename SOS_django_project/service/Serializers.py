


from rest_framework import serializers
from .models import User, Role,College,Course,Faculty,Marksheet,Student,Subject,TimeTable

        
class CollegeSerializers(serializers.ModelSerializer):  
    class Meta:  
        model = College  
        fields = ['id','collegeName','collegeAddress','collegeState','collegeCity','collegePhoneNumber']          
      
class CourseSerializers(serializers.ModelSerializer):  
    class Meta:  
        model = Course  
        fields = ['id','courseName','courseDescription','courseDuration']          

class UserSerializers(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id','firstName','lastName','login_id','password','confirmpassword','dob','address','gender','mobilenumber','role_Id','role_Name']                 

class RoleSerializers(serializers.ModelSerializer):  
    class Meta:  
        model = Role  
        fields = ['name','description'] 

class MarksheetSerializers(serializers.ModelSerializer):  
    class Meta:  
        model = Marksheet  
        fields = ['rollNumber','name','physics','chemistry',' maths','student_ID']                        

class StudentSerializers(serializers.ModelSerializer):  
    class Meta:  
        model = Student  
        fields = ['firstName','lastName','dob','mobileNumber',' email','college_ID','collegeName']                        

class SubjectSerializers(serializers.ModelSerializer):  
    class Meta:  
        model = Subject  
        fields = ['subjectName','subjectDescription','dob','course_ID',' courseName']                        

class TimeTableSerializers(serializers.ModelSerializer):  
    class Meta:  
        model = TimeTable  
        fields = ['examTime','examDate','subject_ID','subjectName',' course_ID','courseName','semester']                        


class AddFacultySerializers(serializers.ModelSerializer):  
    class Meta:  
        model = Faculty  
        fields = ['firstName','lastName','email','password',' address','gender','dob','college_ID','subject_ID','course_ID']                        