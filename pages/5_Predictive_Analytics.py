import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("💵 Funding Analytics")

fig = px.scatter(
    df,
    x="Funding Rounds",
    y="Funding Amount (M USD)",
    color="Industry",
    size="Valuation (M USD)",
    hover_name="Startup Name",
    title="Funding Rounds vs Funding Amount"
)

st.plotly_chart(fig, use_container_width=True)

top10 = df.nlargest(
    10,
    "Funding Amount (M USD)"
)

st.subheader("Top 10 Funded Startups")

st.dataframe(
    top10[
        [
            "Startup Name",
            "Industry",
            "Funding Amount (M USD)",
            "Valuation (M USD)"
        ]
    ]
)

fig2 = px.histogram(
    df,
    x="Funding Amount (M USD)",
    nbins=20,
    title="Funding Distribution"
)

st.plotly_chart(fig2, use_container_width=True)
