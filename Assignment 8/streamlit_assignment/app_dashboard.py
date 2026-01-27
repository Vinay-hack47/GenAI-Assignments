import streamlit as st

st.title("Simple Sales Dashboard")
st.write("Monthly sales overview")

months = ["January", "February", "March", "April","May", "June"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000,
    "May": 2004,
    "June": 8000
}

selected_month = st.selectbox("Select Month", months)

st.metric("Sales", sales[selected_month])

st.bar_chart(list(sales.values()))
