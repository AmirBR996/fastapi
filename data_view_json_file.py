import json 
from fastapi import FastAPI , Path , HTTPException , Query
# HTTP exception is a built in exception in fastapi that return custom http error responses when something wrong with you api
app = FastAPI()
def info():
    with open("patients.json" , "r") as f:
        data = json.load(f)
    return data
@app.get("/")
def hello():
    return {"message" : "This is pathient API"}
@app.get("/about")
def get():
    return {"message" : "This is about patient data"}

@app.get("/data")
def data():
    data = info()
    return data


# if we want to fetch single patient from id
@app.get("/patient/{patient_id}")
# we initialize patient id as string in the function
def patient(patient_id : str = Path(... , description = f"this is a data of patient" ,example = "P001")): 
    #  we can describe endpoints with path functions
    data = info()
    if patient_id in data:
        return data[patient_id]
    # return {"message : patient_id not found in data"} instead of this we can use httpexception
    raise HTTPException(status_code=404 , detail="patient not found in db")

# query parameters: it is used to return results in sorting ,filtering ,  orders,etc . we use it at last of endpoints using ?

@app.get("/sorted_patient")
def sorted(sort_by : str = Query(..., description= "sort on the basis of height , weight or bmi ") , order : str = Query("asc", description=" sorted in asc or desc order  ")):
    valid_fields = ["height" , "weight" , "bmi"]
    if sort_by not in valid_fields:
     raise HTTPException(status_code=400 , description = "invalid field")
    if order not in ["asc" , "desc"]:
     raise HTTPException(status_code=400 , description = "plz choose between asc or desc")
    data = info()
    sorted_order = True if order == "asc" else False
    sorted_data = sorted(data.values() ,key =  lambda x : x.get(sort_by) , reverse = sorted_order)
    return sorted_data



