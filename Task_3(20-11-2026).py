import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("----PART 1 : NUMPY----")

marks=np.array([[75,85,90],
                [67,70,73],
                [82,94,84],
                [55,62,58]])

print("Marks array:")
print(marks)
print("Shape:", marks.shape)

# student average(row wise)
student_avg=marks.mean(axis=1)
print("Student averages:", student_avg)

# subject average(column wise)
subject_avg=marks.mean(axis=0)
print("Subject averages:", subject_avg)

marks_new=marks+5
print("After adding 5 grace marks:")
print(marks_new)

weights=np.array([0.3, 0.3, 0.4])
weighted=np.dot(marks,weights)
print("Weighted scores:", weighted)

print("\n----- PART 2 : PANDAS LOAD-----")

# employees data - I created this myself
# 9 rows, 1 duplicate, 2 salaries missing
emp_data={"emp_id":[1,2,3,4,5,6,7,8,1],
          "name":["Ravi","Priya","Kumar","Anitha","Suresh","Divya","Manoj","Lakshmi","Ravi"],
          "department":["Sales","Sales","HR","HR","IT","IT","IT","Finance","Sales"],
          "salary":[45000,50000,38000,None,60000,65000,None,55000,45000]}

df=pd.DataFrame(emp_data)
df.to_csv("employees.csv",index=False)
print("employees.csv created")

df=pd.read_csv("employees.csv")
print(df)
print("\ninfo():")
print(df.info())
print("\ndescribe():")
print(df.describe())

print("\nloc - first 3 rows, name and salary:")
print(df.loc[0:2,["name","salary"]])

print("\niloc - first 3 rows:")
print(df.iloc[0:3])

print("Before cleaning shape:", df.shape)
print("Missing values:")
print(df.isnull().sum())

median_salary=df["salary"].median()
print("Median salary:", median_salary)
df["salary"]=df["salary"].fillna(median_salary)

df=df.drop_duplicates()
print("After dropping duplicate shape:", df.shape)

df["emp_id"]=df["emp_id"].astype(int)
df["salary"]=df["salary"].astype(int)
print(df)
print(df.dtypes)

print("\n----- PART 4: DEPARTMENTS+GRUOPBY+MERGE -----")

# departments.csv
dept_data={"department":["Sales","HR","IT","Finance","Marketing"],
           "head":["Raj","Meena","Arun","Kavitha","Vikram"],
           "budget":[500000,300000,800000,400000,250000],
           }
dept_df=pd.DataFrame(dept_data)
dept_df.to_csv("departments.csv", index=False)
print(dept_df)

# groupby
grouped=df.groupby("department").agg(
    headcount=("emp_id","count"),
    average_salary=("salary","mean"),
    max_salary=("salary","max")
)
print("\nGroupby result:")
print(grouped)

# merging
grouped=grouped.reset_index()

print("\nInner merge:")
print(pd.merge(grouped, dept_df, on="department", how="inner"))

print("\nLeft merge:")
print(pd.merge(grouped, dept_df, on="department", how="left"))

print("\nOuter merge:")
outer=pd.merge(grouped, dept_df, on="department", how="outer")
print(outer)

print("\nDepartment with no employees:")
no_emp=outer[outer["headcount"].isnull()]
print(no_emp["department"].tolist())

print("\n----- PART5 : CHARTS -----")

# bar chart
plt.figure()
plt.bar(grouped["department"], grouped["headcount"], color="green",label="Headcount")
plt.title("Headcount per Department")
plt.xlabel("Department")
plt.ylabel("Headcount")
plt.legend()
plt.savefig("bar_chart.png")
plt.show()
print("Insight:IT has highest headcount(3), Finance has lowest(1).")

# histogram
plt.figure()
plt.hist(df["salary"],bins=4, color="orange", label="Salary")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("No of Employees")
plt.legend()
plt.savefig("histogram.png")
plt.show()
print("Insight: Most employees salary is between 45000 and 60000.")

# Scatter
plt.figure()
plt.scatter(df["emp_id"],df["salary"],color="red",label="Salary")
plt.title("Emp ID vs Salary")
plt.xlabel("Emp ID")
plt.ylabel("Salary")
plt.legend()
plt.savefig("scatter.png")
plt.show()
print("Insight: Salary does not depend on Emp ID,IT employees earn more.")

# Line chart
plt.figure()
plt.plot(["S1","S2","S3","S4"],student_avg,marker="o",label="Student Avg")
plt.title("Student Averages")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.legend()
plt.savefig("line_chart.png")
plt.show()
print("Insight:Student 3 got highest average, student 4 got lowest.")

print("\nTask 3 Done")