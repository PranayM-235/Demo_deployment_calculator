
import streamlit as st
import requests

st.title("🧮 Full Stack Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox(
    "Select operation",
    ["add", "subtract", "multiply", "divide"]
)

if st.button("Calculate"):
    url = "http://127.0.0.1:8000/calculate"

    params = {
        "num1": num1,
        "num2": num2,
        "operation": operation
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "result" in data:
        st.success(f"Result: {data['result']}")
    else:
        st.error(data["error"])