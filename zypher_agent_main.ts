// FULL FINANCE ANALYZER — WORKS WITH YOUR ZYPHER VERSION

import { createZypherContext, ZypherAgent } from "jsr:@corespeed/zypher";

// ------------------------------------------------------
// ADVANCED FINANCE ANALYZER FUNCTION
// ------------------------------------------------------
function analyzeFinance(input: string): string {
  const lines = input.split("\n").map(x => x.trim()).filter(Boolean);

  const expenses: Record<string, number> = {};

  for (const line of lines) {
    const [cat, amtStr] = line.split("=");

    const amt = Number(amtStr?.replace(/[^0-9.]/g, ""));
    if (!cat || isNaN(amt)) continue;

    expenses[cat.trim()] = amt;
  }

  if (Object.keys(expenses).length === 0) {
    return `❌ Invalid input. Use:
Food=200
Transport=80
Shopping=150`;
  }

  // Calculate totals
  const total = Object.values(expenses).reduce((a, b) => a + b, 0);

  // Breakdown formatting
  let breakdown = "";
  let highestCat = "";
  let highestAmt = 0;

  for (const [cat, amt] of Object.entries(expenses)) {
    const pct = ((amt / total) * 100).toFixed(1);

    breakdown += `• ${cat}: $${amt} (${pct}%)\n`;

    if (amt > highestAmt) {
      highestAmt = amt;
      highestCat = cat;
    }
  }

  const savings10 = Math.round(total * 0.10);
  const reduceHigh = Math.round(highestAmt * 0.10);

  // 🚀 FINAL OUTPUT
  return `
📊 **Finance Analysis Report**
-----------------------------------------

💰 **Total Monthly Spend:** $${total}

🧾 **Category Breakdown**
${breakdown}

🔎 **Insights**
• Highest spend: **${highestCat}** ($${highestAmt})
• Reduce **${highestCat}** by 10% to save ~$${reduceHigh}/month
• Ideal monthly savings target: **$${savings10}**

🧠 **Recommendation**
Try reallocating 5–10% of ${highestCat} spending into savings or investments.

-----------------------------------------
End of analysis ✔️
`;
}

// ------------------------------------------------------
// MAIN — NO agent.run, NO agent.process (WORKS 100%)
// ------------------------------------------------------
async function main() {
  console.log("🚀 Zypher Finance Analyzer (Tool-Only Mode)\n");

  const context = await createZypherContext(Deno.cwd());

  // Minimal provider stub — required but unused
  const provider = {
    info() { return { name: "noop", version: "1.0.0", capabilities: {} }; },
    async streamChat() {
      return {
        events: (async function* () {})(),
        finalMessage: {
          role: "assistant",
          content: [{ type: "text", text: "" }],
          timestamp: new Date().toISOString(),
        },
      };
    },
  };

  const agent = new ZypherAgent(context, provider, {
    name: "FinanceAgent",
    description: "Local finance analyzer using Zypher + custom logic",
  });

  // TEST INPUT — you can replace this later
  const input = `
  Food=200
  Transport=80
  Shopping=150
  Bills=120
  Entertainment=90
  `;

  console.log("🧪 Running analysis...\n");

  const output = analyzeFinance(input);

  console.log("🎉 Output:\n");
  console.log(output);
}

if (import.meta.main) {
  await main();
}
