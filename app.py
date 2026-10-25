import streamlit as st
from portfolio_visuals import render_visuals
ALLOWED_TOOLS = {"summarize", "count_words"}

def run_tool(name: str, text: str) -> str:
    if name not in ALLOWED_TOOLS:
        raise ValueError("Tool is not on the allowlist.")
    if name == "summarize":
        return "Summary: " + " ".join(text.split()[:40])
    if name == "count_words":
        return f"Word count: {len(text.split())}"
    raise ValueError("Unsupported tool")

def run_workflow(task: str, tool_names: list[str], approved: bool) -> list[dict]:
    if not approved:
        return [{"status": "waiting_for_approval", "message": "Approve this workflow before execution."}]
    output = []
    for name in tool_names:
        output.append({"tool": name, "status": "success", "result": run_tool(name, task)})
    return output

st.set_page_config(page_title="Agentic Workflow", page_icon="ðŸ§­")
render_visuals('04_agentic_workflow')
st.title("Agentic Workflow Automation")
st.caption("Bounded demo workflow; tools are local and allowlisted.")
task = st.text_area("Task text", "Summarize this text and count its words.")
tools = st.multiselect("Allowed tools to run", sorted(ALLOWED_TOOLS), default=["summarize", "count_words"])
approved = st.checkbox("I approve running these local tools")
if st.button("Run workflow", type="primary"):
    try:
        st.json(run_workflow(task, tools, approved))
    except ValueError as e:
        st.error(str(e))

