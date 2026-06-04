import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("🏭 Industry Analysis")

industry_funding = df.groupby(
    "Industry"
)["Funding Amount (M USD)"].sum().reset_index()

fig = px.bar(
    industry_funding,
    x="Industry",
    y="Funding Amount (M USD)",
    color="Funding Amount (M USD)",
    title="Funding by Industry"
)

st.plotly_chart(fig, use_container_width=True)

industry_valuation = df.groupby(
    "Industry"
)["Valuation (M USD)"].mean().reset_index()

fig2 = px.pie(
    industry_valuation,
    names="Industry",
    values="Valuation (M USD)",
    title="Average Valuation Share"
)

st.plotly_chart(fig2, use_container_width=True)

industry_revenue = df.groupby(
    "Industry"
)["Revenue (M USD)"].mean().reset_index()

fig3 = px.bar(
    industry_revenue,
    x="Industry",
    y="Revenue (M USD)",
    color="Revenue (M USD)",
    title="Average Revenue by Industry"
)

st.plotly_chart(fig3, use_container_width=True)

highest = industry_funding.loc[
    industry_funding["Funding Amount (M USD)"].idxmax(),
    "Industry"
]

st.success(f"Highest funded industry: {highest}")
