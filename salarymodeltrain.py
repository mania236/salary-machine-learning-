import pandas
db = pandas.read_csv('SalaryData.csv')
y = db['Salary']
x = db['YearsExperience']
x = x.values
x = x.reshape(30,1)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
import joblib
joblib.dump(model ,"salary2.pk1")
