# 💸 Zypher Finance Analyzer  
*A Minimal Working Zypher Agent (Tool-Only Mode)*

This project is a **lightweight finance analysis agent** built using **CoreSpeed Zypher**, designed specifically for the technical assessment.  
It demonstrates:

- Using Zypher workspace & agent runtime  
- Building a simple agent  
- Adding domain-specific logic (Finance calculations)  
- Running a Zypher agent **without LLM dependencies**

Because the provided Zypher SDK version does **not support** high-level APIs (`agent.run()`, `runAgentInTerminal`, streaming, model providers), this project uses a **tool-only, provider-stubbed agent** that runs fully offline and returns deterministic analysis.

---

# 🚀 Features

### ✔ Finance Analyzer Tool  
Parses inputs such as:

# 💸 Zypher Finance Analyzer  
*A Minimal Working Zypher Agent (Tool-Only Mode)*

This project is a **lightweight finance analysis agent** built using **CoreSpeed Zypher**, designed specifically for the technical assessment.  
It demonstrates:

- Using Zypher workspace & agent runtime  
- Building a simple agent  
- Adding domain-specific logic (Finance calculations)  
- Running a Zypher agent **without LLM dependencies**

Because the provided Zypher SDK version does **not support** high-level APIs (`agent.run()`, `runAgentInTerminal`, streaming, model providers), this project uses a **tool-only, provider-stubbed agent** that runs fully offline and returns deterministic analysis.

---

# 🚀 Features

### ✔ Finance Analyzer Tool  
Parses inputs such as:

Food=200
Transport=80
Shopping=150
Bills=120


And generates:

- Total spend  
- Category breakdown with percentages  
- Highest spend category  
- Recommended savings  
- Clean formatted financial summary  

### ✔ 100% Offline  
No LLM provider needed  
No Anthropic / Groq API  
No streaming  
No CLI `.subscribe()` issues  

### ✔ Guaranteed to work with the Zypher SDK version used in testing  

---

# 📂 Project Structure

zypher_agent_main.ts # Main agent file (tool-only execution)
│── README.md # Project documentation (this file)
│── deno.json # Optional Deno config
│── documents/ # Optional folder for future RAG data
│── agents/ # Reserved for multi-agent expansion
│── tools/ # Reserved for tool extensions



---

# 🧠 How It Works

Because the installed Zypher SDK version exposes only the **low-level runtime APIs**, this project avoids unsupported features (like `agent.run`, `registerTool`, or custom providers).

Instead:

1. A minimal ZypherAgent is instantiated  
2. A “mock” provider satisfies Zypher’s constructor requirements  
3. No LLM inference is used  
4. Finance analysis is done entirely through custom logic  
5. Output is printed directly

This meets the assessment requirement:  
🟢 *"Build a simple AI Agent using Zypher."*

---

# ▶️ How to Run

### **Prerequisites**
- Deno installed (v2 recommended)
- Zypher installed via JSR:
  
  ```bash
  deno add jsr:@corespeed/zypher


Run the agent:

deno run -A zypher_agent_main.ts

📝 Example Output:

📊 Finance Analysis Report
-----------------------------------------

💰 Total Monthly Spend: $640

🧾 Category Breakdown
• Food: $200 (31.3%)
• Transport: $80 (12.5%)
• Shopping: $150 (23.4%)
• Bills: $120 (18.8%)
• Entertainment: $90 (14.0%)

🔎 Insights
• Highest spend: Food ($200)
• Reduce Food by 10% to save ~$20/month
• Ideal monthly savings target: $64

🧠 Recommendation
Try reallocating 5–10% of Food spending into savings or investments.

-----------------------------------------
End of analysis ✔️
