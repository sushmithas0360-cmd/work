import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("💰 Profitability Analysis")

df["Profit Status"] = df["Profitable"].map(
    {1: "Profitable", 0: "Not Profitable"}
)

fig = px.pie(
    df,
    names="Profit Status",
    title="Profitability Distribution"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(
    df,
    x="Profit Status",
    y="Revenue (M USD)",
    color="Profit Status",
    title="Revenue Comparison"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.box(
    df,
    x="Profit Status",
    y="Valuation (M USD)",
    color="Profit Status",
    title="Valuation Comparison"
)

st.plotly_chart(fig3, use_container_width=True)

profitable_count = len(
    df[df["Profitable"] == 1]
)

st.metric(
    "Profitable Startups",
    profitable_count
)
