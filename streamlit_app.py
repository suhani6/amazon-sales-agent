import streamlit as st
from agent.agent_builder import agent

st.set_page_config(page_title="Amazon Sales AI Agent", layout="centered")
st.title("📈 Amazon Sales AI Agent")
st.caption("Ask natural language questions about sales performance")

# Text input
query = st.text_input("Enter your question:", placeholder="e.g. What are the top 5 products?")

# Submit
if st.button("Ask Agent") and query:
    with st.spinner("Thinking..."):
        try:
            response = agent.run(query)
            st.success("✅ Answer:")
            st.write(response)

            # If agent saved a chart image, show it
            if "chart" in response.lower() or "saved" in response.lower():
                if "revenue" in response.lower():
                    st.image("monthly_revenue_trend.png")
                elif "category" in response.lower():
                    st.image("category_distribution.png")

        except Exception as e:
            st.error(f"Error: {e}")
