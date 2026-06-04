import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("🌍 Regional Insights")

region_funding = df.groupby(
    "Region"
)["Funding Amount (M USD)"].sum().reset_index()

fig = px.treemap(
    region_funding,
    path=["Region"],
    values="Funding Amount (M USD)",
    title="Funding Distribution by Region"
)

st.plotly_chart(fig, use_container_width=True)

region_val = df.groupby(
    "Region"
)["Valuation (M USD)"].mean().reset_index()

fig2 = px.bar(
    region_val,
    x="Region",
    y="Valuation (M USD)",
    color="Valuation (M USD)",
    title="Average Valuation by Region"
)

st.plotly_chart(fig2, use_container_width=True)

region_rev = df.groupby(
    "Region"
)["Revenue (M USD)"].mean().reset_index()

fig3 = px.bar(
    region_rev,
    x="Region",
    y="Revenue (M USD)",
    color="Revenue (M USD)",
    title="Average Revenue by Region"
)

st.plotly_chart(fig3, use_container_width=True)
