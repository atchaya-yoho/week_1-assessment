import csv

# reading file
data=[]
with open ("employees.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        row["salary"]=int(row["salary"])
        data.append(row)

# bonus
def bonus(salary,rate=0.1,*extras,**options):
    amt=salary*rate+sum(extras)
    if "cap" in options:
        if amt>options["cap"]:
            amt=options["cap"]
        return amt

# custom error
class InvalidSalaryError(Exception):
    pass

# employee class
class Employee:
    def __init__(self,name,salary):
        if salary<0:
            raise InvalidSalaryError("Invalid salary:"+str(salary))
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
    def get_details(self):
        return self.name + "-" + str(self.salary)

# manager class
class Manager(Employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def get_details(self):
        return self.name+ "-" +str(self.salary)+", Team: "+str(self.team_size)

# salary above 50000
high_sal=[x["name"] for x in data if x["salary"]>50000]
print("Above 50000:",high_sal)

# 10% hike
new_salaries=list(map(lambda x: x["salary"]*1.1, data))
print(new_salaries)

# chennai only
chennai_list=list(filter(lambda x: x["city"]=="Chennai",data))
chennai_names=[x["name"] for x in chennai_list]
print("Chennai:", chennai_names)

# error handling
try:
    emp1=Employee("Ravi",-500)
except InvalidSalaryError as err:
    print("Error:",err)
finally:
    print("Transaction finished")

# loop
salaries=[30000,0,45000,60000,75000,90000,52000]
for s in salaries:
    if s==0:
        continue
    print(s)
    if s>85000:
        break

m1=Manager("Karthik",90000,5)
print(m1.get_details())
print(m1.annual_salary())
b1=bonus(50000,0.1,2000, cap=8000)
print(b1)