import pickle
data = {
    "Devansh" : "Java",
    "DevanshBot" : "Python"
}

with open("Dev.pkl", 'wb') as f:
    pickle.dump(data, f)
