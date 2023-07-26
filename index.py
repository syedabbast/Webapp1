import streamlit as stst
import streamlit as st


st.title ("Python WebApp")
def main():
    st.title("Python WebApp Calculator")
    
    st.title("Simple Calculator with Submit Button")
    

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    st.title("Calculator")

    num1 = st.number_input("Enter the first number:", step=0.1)
    num2 = st.number_input("Enter the second number:", step=0.1)

    operation = st.selectbox("Select an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))
    
    
    result = None

    if st.button("Calculate"):
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)

    if result is not None:
        st.success(f"Result: {result}")

if __name__ == '__main__':
    main()
