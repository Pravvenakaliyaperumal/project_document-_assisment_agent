# agents/agent_core.py
from typing import Dict, Any, Callable
import google.generativeai as genai


class BaseAgent:
    def __init__(self, name: str, system_prompt: str, tools: Dict[str, Callable]):
        self.name = name
        self.system_prompt = system_prompt
        self.tools = tools

    def run(self, user_input: str) -> str:
        """Processes user input using system prompt + tools."""
        # Check if user requested a tool explicitly
        for key, tool_fn in self.tools.items():
            if key in user_input.lower():
                return tool_fn(user_input)

        # Otherwise, use the LLM
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
            f"System: {self.system_prompt}\nUser: {user_input}"
        )
        return response.text
