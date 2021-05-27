import joblib
model = joblib.load("salary.pk1")
print('enter your experience')
e = input()
e = float(e)
x = model.predict([[e]])
print(x)
