from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running 🚀"}

@app.get("/calculate")
def calculate(num1: float, num2: float, operation: str):

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            return {"error": "Cannot divide by zero"}
    else:
        return {"error": "Invalid operation"}

    return {"result": result}