# agents/finance_agent.py
from .agent_core import BaseAgent
from typing import Dict, Callable


def create_finance_agent(tools: Dict[str, Callable]):
    system_prompt = """
    You are a Finance AI Agent. You analyze transactions, expenses, profits,
    financial health, risk signals, and provide actionable insights.
    Be accurate, numeric, formatted, and concise.
    """
    return BaseAgent(name="finance_agent", system_prompt=system_prompt, tools=tools)
