
import streamlit as st

def benefit_rule_engine(plan_type, service_type, deductible_met):
    # Normalize inputs
    plan_type = plan_type.lower()
    service_type = service_type.lower()
    deductible_met = deductible_met.lower() in ['yes', 'true', '1']

    # Rule logic
    if plan_type == "gold" and service_type in ["dental", "vision"] and deductible_met:
        return "Approved"
    elif plan_type == "silver" and service_type == "general" and deductible_met:
        return "Approved"
    elif plan_type == "bronze" and service_type == "general":
        return "Approved with Copay"
    else:
        return "Denied"

st.set_page_config(page_title="Benefit Rule Engine")
st.title("🧠 Healthcare Benefit Rule Engine")

st.markdown("Simulate a healthcare claim decision based on plan, service type, and deductible status.")

plan = st.selectbox("Select your plan type:", ["Gold", "Silver", "Bronze"])
service = st.selectbox("Select service type:", ["General", "Dental", "Vision"])
deductible = st.selectbox("Is deductible met?", ["Yes", "No"])

if st.button("Evaluate Claim"):
    result = benefit_rule_engine(plan, service, deductible)
    st.success(f"Claim Decision: **{result}**")
