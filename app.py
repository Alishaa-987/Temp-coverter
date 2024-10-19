import streamlit as st

# Function to convert temperatures
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

# Streamlit app layout
st.set_page_config(page_title="Temperature Converter", layout="centered")
st.title("🌡️ Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")
st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line for separation

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stTextInput>div>input {
        font-size: 16px;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ccc;
        transition: border-color 0.3s ease;
    }
    .stTextInput>div>input:focus {
        border-color: #4CAF50; /* Green border on focus */
    }
    </style>
""", unsafe_allow_html=True)

# User selection for conversion type
conversion_type = st.selectbox("Select conversion type:",
    ["Celsius to Fahrenheit",
     "Fahrenheit to Celsius",
     "Celsius to Kelvin",
     "Kelvin to Celsius",
     "Fahrenheit to Kelvin",
     "Kelvin to Fahrenheit"])

# Input temperature based on selected conversion type
if conversion_type == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius:", format="%.2f", step=0.1)
    if st.button("Convert"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")

elif conversion_type == "Fahrenheit to Celsius":
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f", step=0.1)
    if st.button("Convert"):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")

elif conversion_type == "Celsius to Kelvin":
    celsius = st.number_input("Enter temperature in Celsius:", format="%.2f", step=0.1)
    if st.button("Convert"):
        kelvin = celsius_to_kelvin(celsius)
        st.success(f"{celsius:.2f}°C is {kelvin:.2f}K")

elif conversion_type == "Kelvin to Celsius":
    kelvin = st.number_input("Enter temperature in Kelvin:", format="%.2f", step=0.1)
    if st.button("Convert"):
        celsius = kelvin_to_celsius(kelvin)
        st.success(f"{kelvin:.2f}K is {celsius:.2f}°C")

elif conversion_type == "Fahrenheit to Kelvin":
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f", step=0.1)
    if st.button("Convert"):
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        st.success(f"{fahrenheit:.2f}°F is {kelvin:.2f}K")

elif conversion_type == "Kelvin to Fahrenheit":
    kelvin = st.number_input("Enter temperature in Kelvin:", format="%.2f", step=0.1)
    if st.button("Convert"):
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        st.success(f"{kelvin:.2f}K is {fahrenheit:.2f}°F")
