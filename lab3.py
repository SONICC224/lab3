#!/usr/bin/env python
# coding: utf-8

# In[1]:


def conform(fav):
    fav = 42
    return fav


# In[2]:


if __name__== "__main__":
    print('welcome!')
    fav =7
    conform(fav)
    print("my favorite # is " , fav)


# In[3]:


student={'a':28, 'b':25, 'c':32, 'd':25}
def test(student):
    new={'e':30, 'f':28}
    student.update(new)
    print("inside the function ",student)
    return
test(student)
print("outside the function:",student)


# In[6]:


class Student:
    
    def __init__(self,name):
        self.name=name
        self.course_list= []
    def add(self, new_course):
        self.course_list.append(new_course)

class Person:
    pass

std=Student("Set_here_your_name")
txt = input("Type")#input
std.add(txt)
print(std.course_list)


# In[5]:


class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        
class Professor(Person):
    def __init__(self,fname,lname):#E2.3
        self.department='Information System'
        Person.__init__(self,fname,lname)
        
mhd = Professor("Mohammed","Ali")
mhd.printname()
print(mhd.department)


# In[ ]:




