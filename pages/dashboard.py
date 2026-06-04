st.set_page_config(layout="wide")

df = pd.read_csv("data/startup_data.csv")

st.title("🚀 Startup Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Startups", len(df))

col2.metric(
    "Total Funding",
    f"${df['Funding Amount (M USD)'].sum():,.0f} M"
)

col3.metric(
    "Average Valuation",
    f"${df['Valuation (M USD)'].mean():,.0f} M"
)

col4.metric(
    "Average Revenue",
    f"${df['Revenue (M USD)'].mean():,.0f} M"
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        df,
        x="Industry",
        title="Industry Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.histogram(
        df,
        x="Region",
        title="Regional Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

fig = px.scatter(
    df,
    x="Revenue (M USD)",
    y="Valuation (M USD)",
    color="Industry",
    size="Funding Amount (M USD)",
    hover_name="Startup Name",
    title="Revenue vs Valuation"
)
