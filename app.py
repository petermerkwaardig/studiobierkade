import streamlit as st
from datetime import datetime

def calculate_average_monthly_salary(yearly_salaries):
    total_salary = sum(yearly_salaries)
    average_monthly_salary = total_salary / (len(yearly_salaries) * 12)
    return round(average_monthly_salary, 2)

def calculate_severance_payment(start_date, end_date, monthly_salary):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    total_months = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month
    years = total_months // 12
    months = total_months % 12
    partial_year = months / 12
    transitievergoeding_per_year = (1/3) * monthly_salary
    transitievergoeding = (years + partial_year) * transitievergoeding_per_year
    correctiefactor = 1.8
    severance_payment = transitievergoeding * correctiefactor
    return round(severance_payment, 2)

st.title("Ontslagvergoeding Calculator")

start_date = st.text_input("Startdatum (YYYY-MM-DD)", "2020-03-01")
end_date = st.text_input("Einddatum (YYYY-MM-DD)", "2024-12-01")
salary_2020 = st.number_input("Bruto jaarinkomen 2020", value=50000)
salary_2021 = st.number_input("Bruto jaarinkomen 2021", value=55000)
salary_2022 = st.number_input("Bruto jaarinkomen 2022", value=60000)
salary_2023 = st.number_input("Bruto jaarinkomen 2023", value=65000)

if st.button("Bereken"):
    yearly_salaries = [salary_2020, salary_2021, salary_2022, salary_2023]
    average_monthly_salary = calculate_average_monthly_salary(yearly_salaries)
    severance_payment = calculate_severance_payment(start_date, end_date, average_monthly_salary)
    st.write(f"Gemiddeld bruto maandsalaris: €{average_monthly_salary}")
    st.write(f"Ontslagvergoeding: €{severance_payment}")
