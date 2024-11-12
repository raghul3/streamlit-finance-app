import streamlit as st


st.title("Assets")

# Initialize session state for real estate values list
if "real_estate_values" not in st.session_state:
    st.session_state.real_estate_values = []


st.header("Equity")
equity = st.number_input("Enter your equity investment:", min_value=0.0, step=0.01)


st.header("Real Estate")
if st.button("Add Real Estate Investment"):
    st.session_state.real_estate_values.append(0.0)

#To display the real estate input fields
for i in range(len(st.session_state.real_estate_values)):
    st.session_state.real_estate_values[i] = st.number_input(
        f"Real Estate Investment {i+1}",
        min_value=0.0,
        step=0.01,
        key=f"real_estate_{i}"#gives each input a unique key
    )

st.header("Passive Income Assets")
passive_income_assets = st.number_input("Enter passive income asset value:", min_value=0.0, step=0.01)

st.header("Debt")
debt = st.number_input("Enter debt amount:", min_value=0.0, step=0.01)

st.header("Alternative Investments")
alternative_investments = st.number_input("Enter alternative investment value:", min_value=0.0, step=0.01)

# Showing all inputs
st.subheader("Summary of Your Inputs")
st.write(f"Equity: {equity}")
st.write(f"Real Estate Investments: {st.session_state.real_estate_values}")
st.write(f"Passive Income Assets: {passive_income_assets}")
st.write(f"Debt: {debt}")
st.write(f"Alternative Investments: {alternative_investments}")
