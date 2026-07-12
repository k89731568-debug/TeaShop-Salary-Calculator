import streamlit as st

from constants import ROLES
from salary import calculate_salary

st.set_page_config(
    page_title="Tea Shop Salary Calculator",
    page_icon="🍵",
)

st.title("🍵 Tea Shop Salary Calculator")

st.write("Enter the employee information below.")

required_hours = st.number_input(
    "Required Hours",
    value=229.5
)

role = st.selectbox(
    "Employee Role",
    options=range(len(ROLES)),
    format_func=lambda x: ROLES[x]
)

performance = st.number_input(
    "Performance Bonus",
    value=400.0
)

worked_hours = st.number_input(
    "Worked Hours",
    value=229.5
)

double_ot = st.number_input(
    "Double OT Hours",
    value=0.0
)

triple_ot = st.number_input(
    "Triple OT Hours",
    value=0.0
)

if st.button("Calculate Salary"):

    result = calculate_salary(
        role,
        required_hours,
        performance,
        worked_hours,
        double_ot,
        triple_ot,
    )

    st.subheader("Salary Breakdown")

    total_salary = 0

    for item, amount in result.items():
        st.write(f"**{item}:** ¥{amount}")
        total_salary += amount

    st.divider()

    st.success(f"Total Salary: ¥{total_salary}")