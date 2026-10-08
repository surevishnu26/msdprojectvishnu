from fastapi import FastAPI
app=FastAPI()
@app.get("/getStudents")
def getStudents():
    return "get student method called"
@app.post("/addStudent")
def addStudent():
    return "add student method called"
@app.put("/updateStudent")
def updatestudent():
    return"update student method called"
@app.delete("/deleteStudent")
def deletestudent():
    return"delete student method called"