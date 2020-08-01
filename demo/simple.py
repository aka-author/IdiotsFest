# * * ** *** ***** ******** ************* *********************
# The Festival of Idiots. A simple machine learning algorithm
# 
# Project: IdiotFest ML
# Part:    Demo scripts
# Module:  simple.py                                  (\_/)
#                                                     (^.^)
# * * ** *** ***** ******** ************* *********************

import sys

sys.path.append("../py")

from idiotfest import *


def assemble_teaching_array():

    teaching_array = [ \
    
        {"city" : "Kiev",   "job" : "Programmer", "age" : 50, "salary" : 100000}, \
        {"city" : "Kiev",   "job" : "Programmer", "age" : 40, "salary" : 125000}, \
        {"city" : "Kiev",   "job" : "Programmer", "age" : 30, "salary" :  80000}, \
        {"city" : "Moscow", "job" : "Programmer", "age" : 50, "salary" : 140000}, \
        {"city" : "Moscow", "job" : "Programmer", "age" : 40, "salary" : 160000}, \
        {"city" : "Moscow", "job" : "Programmer", "age" : 30, "salary" : 120000}, \
        
        
        {"city" : "Kiev",   "job" : "Accountant", "age" : 50, "salary" :  70000}, \
        {"city" : "Kiev",   "job" : "Accountant", "age" : 40, "salary" :  90000}, \
        {"city" : "Kiev",   "job" : "Accountant", "age" : 30, "salary" :  50000}, \
        {"city" : "Moscow", "job" : "Accountant", "age" : 50, "salary" :  90000}, \
        {"city" : "Moscow", "job" : "Accountant", "age" : 40, "salary" : 110000}, \
        {"city" : "Moscow", "job" : "Accountant", "age" : 30, "salary" :  70000}, \
        
        {"city" : "Kiev",   "job" : "Janitor",    "age" : 50, "salary" :  60000}, \
        {"city" : "Kiev",   "job" : "Janitor",    "age" : 40, "salary" :  40000}, \
        {"city" : "Kiev",   "job" : "Janitor",    "age" : 30, "salary" :  30000}, \
        {"city" : "Moscow", "job" : "Janitor",    "age" : 50, "salary" :  80000}, \
        {"city" : "Moscow", "job" : "Janitor",    "age" : 40, "salary" :  60000}, \
        {"city" : "Moscow", "job" : "Janitor",    "age" : 30, "salary" :  40000}  \
        
    ]    
        
    return teaching_array 

        
def test():

    # 1. Assembling a jury
    jury = IdiotFestJuri("salary")
    jury.append_judge(Idiot("city", "string"))
    jury.append_judge(Idiot("job", "string"))
    jury.append_judge(Idiot("age", "numeric"))
    
    # 2. Teaching jury members
    for attendee in assemble_teaching_array():
        jury.accept_attendee(IdiotFestAttendee(attendee))
        
    # 3. Evaluating an appicant    
    applicant = IdiotFestAttendee({"city" : "Moscow", "job" : "Programmer", "age" : 65})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))
    
    applicant = IdiotFestAttendee({"city" : "Moscow", "job" : "Programmer", "age" : 41})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))
    
    applicant = IdiotFestAttendee({"city" : "Kiev", "job" : "Programmer", "age" : 41})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))
    
    applicant = IdiotFestAttendee({"city" : "Moscow", "job" : "Programmer", "age" : 37})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))
    
    applicant = IdiotFestAttendee({"city" : "Moscow", "job" : "Programmer", "age" : 25})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))
    
    applicant = IdiotFestAttendee({"city" : "Moscow", "job" : "Programmer", "age" : 18})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))
    
    applicant = IdiotFestAttendee({"city" : "Kiev", "job" : "Accountant", "age" : 45})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))  

    applicant = IdiotFestAttendee({"city" : "Moscow", "job" : "Janitor", "age" : 44})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))   
    
    applicant = IdiotFestAttendee({"city" : "Moscow", "job" : "Janitor", "age" : 80})   
    print(applicant._prop_values, jury.evaluate_attendee(applicant))   
       
test()        
    