
# tools/workflow_executor.py

from zypher.tools import Tool

class WorkflowExecutor(Tool):
    """
    A general-purpose workflow execution tool used by FinanceAgent,
    MedicaidAgent, and CoordinatorAgent.

    This tool simulates real-world decisioning workflows such as:
    - Calculating simple financial metrics
    - Checking eligibility for Medicaid based on income
    - Performing numeric validations or business-rule executions

    Agents call this tool when they need to go beyond Q&A and actually
    execute a small task or calculation.
    """

    name = "workflow_executor"
    description = "Executes predefined workflows for finance and medicaid operations."

    def run(self, workflow_name: str, **kwargs):
        workflow_name = workflow_name.lower()

        # --------------------------------------------------------------------
        # 🏦 FINANCE WORKFLOWS
        # --------------------------------------------------------------------
        if workflow_name == "calculate_simple_interest":
            principal = kwargs.get("principal")
            rate = kwargs.get("rate")
            time = kwargs.get("time")

            if None in (principal, rate, time):
                return "Missing required parameters for interest calculation."

            try:
                interest = (principal * rate * time) / 100
                return f"The calculated simple interest is: {interest}"
            except Exception as e:
                return f"Error during interest calculation: {e}"

        # --------------------------------------------------------------------
        # 🏥 MEDICAID WORKFLOWS
        # --------------------------------------------------------------------
        if workflow_name == "medicaid_income_check":
            income = kwargs.get("income")
            threshold = kwargs.get("threshold", 18000)

            if income is None:
                return "Missing income value for Medicaid eligibility check."

            eligible = income <= threshold

            if eligible:
                return (
                    f"Based on the provided income (${income}), "
                    f"the applicant meets the Medicaid eligibility threshold (${threshold})."
                )
            else:
                return (
                    f"With an income of ${income}, the applicant exceeds the "
                    f"Medicaid eligibility threshold (${threshold})."
                )

        # --------------------------------------------------------------------
        # DEFAULT: Unknown workflow
        # --------------------------------------------------------------------
        return f"Unknown workflow: '{workflow_name}'. Available workflows are: " \
               "calculate_simple_interest, medicaid_income_check."
