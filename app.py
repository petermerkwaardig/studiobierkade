import streamlit as st
from datetime import datetime

# Functies voor berekeningen
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

# Streamlit interface
st.title('Hoeveel krijg je mee?')

start_date = st.text_input('Startdatum (YYYY-MM-DD):', 'YYYY-MM-DD')
end_date = st.text_input('Einddatum (YYYY-MM-DD):', 'YYYY-MM-DD')

try:
    start_year = datetime.strptime(start_date, '%Y-%m-%d').year
    end_year = datetime.strptime(end_date, '%Y-%m-%d').year

    st.write("Vul je bruto jaarinkomen in voor elk jaar van je dienstverband:")
    yearly_salaries = []
    for year in range(start_year, end_year + 1):
        salary = st.number_input(f'Bruto {year}:', min_value=0.0, step=0.01)
        yearly_salaries.append(salary)

    if st.button('Bereken vergoeding'):
        if yearly_salaries and start_date != 'YYYY-MM-DD' and end_date != 'YYYY-MM-DD':
            average_monthly_salary = calculate_average_monthly_salary(yearly_salaries)
            severance_payment = calculate_severance_payment(start_date, end_date, average_monthly_salary)
            st.write(f"Gemiddeld bruto maandsalaris: €{average_monthly_salary}")
            st.write(f"Ontslagvergoeding: €{severance_payment}")
        else:
            st.write("Vul alle velden correct in.")
except Exception as e:
    st.write("Hoe lang werkte je bij Lifetri?")
