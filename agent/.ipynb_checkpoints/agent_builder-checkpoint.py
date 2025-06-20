from langchain.agents import Tool, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_key

# Load your analysis tools
from tools import analysis_tools as at

# Wrap each Python function as a LangChain tool
tools = [
    Tool(
        name="Get Monthly Revenue",
        func=lambda q: str(at.get_total_revenue_by_month()),
        description="Returns total revenue for each month"
    ),
    Tool(
        name="Get Top Products",
        func=lambda q: str(at.get_top_n_products(5)),
        description="Returns top 5 best-selling products"
    ),
    Tool(
        name="Plot Monthly Revenue",
        func=lambda q: at.plot_monthly_revenue_trend(),
        description="Saves a line chart showing revenue trend month by month"
    ),
    Tool(
        name="Average Profit by Region",
        func=lambda q: str(at.get_average_profit_by_region()),
        description="Returns average profit margin grouped by region"
    ),
    Tool(
        name="Category Distribution Chart",
        func=lambda q: at.plot_category_distribution(),
        description="Saves a pie chart of product category distribution"
    ),
    Tool(
        name="Sales by Category",
        func=lambda q: str(at.get_sales_by_category()),
        description="Returns total sales grouped by product category"
    ),
    Tool(
        name="Order Status Breakdown",
        func=lambda q: str(at.get_order_status_breakdown()),
        description="Returns count of completed, returned, or cancelled orders"
    ),
]

# Set up the LLM
llm = ChatOpenAI(temperature=0, model_name="gpt-4")  # or "gpt-3.5-turbo"

# Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
