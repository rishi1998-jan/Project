

from service.models import TimeTable
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService

'''  
It contains Student business logics.   
'''
class TimeTableService(BaseService):
    def search(self,params):
        q = self.get_model().objects.filter()
        

        val = params.get("examTime",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( examTime = val)
            

        val = params.get("examDate",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( examDate = val)
           
       

        val = params.get("subjectName",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( subjectName = val)
           
       

        val = params.get("courseName",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( courseName = val)

        val = params.get("semester",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( semester = val)
        
        return q

    def get_model(self):
        return TimeTable
