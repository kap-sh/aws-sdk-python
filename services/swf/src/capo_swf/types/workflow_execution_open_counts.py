"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionOpenCounts``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.count
    import capo_swf.types.open_decision_tasks_count


class WorkflowExecutionOpenCounts(TypedDict, closed=True):
    open_activity_tasks: "capo_swf.types.count.Count"
    """<p>The count of activity tasks whose status is <code>OPEN</code>.</p>"""
    open_decision_tasks: (
        "capo_swf.types.open_decision_tasks_count.OpenDecisionTasksCount"
    )
    """<p>The count of decision tasks whose status is OPEN. A workflow execution can have at most one open decision task.</p>"""
    open_timers: "capo_swf.types.count.Count"
    """<p>The count of timers started by this workflow execution that have not fired yet.</p>"""
    open_child_workflow_executions: "capo_swf.types.count.Count"
    """<p>The count of child workflow executions whose status is <code>OPEN</code>.</p>"""
    open_lambda_functions: "capo_swf.types.count.Count"
    """<p>The count of Lambda tasks whose status is <code>OPEN</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionOpenCounts) -> dict:
    out: dict = {}
    out["openActivityTasks"] = value.get("open_activity_tasks", 0)
    out["openDecisionTasks"] = value.get("open_decision_tasks", 0)
    out["openTimers"] = value.get("open_timers", 0)
    out["openChildWorkflowExecutions"] = value.get("open_child_workflow_executions", 0)
    out["openLambdaFunctions"] = value.get("open_lambda_functions", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionOpenCounts:
    out: WorkflowExecutionOpenCounts = {}  # type: ignore[typeddict-item]
    if "openActivityTasks" in data:
        out["open_activity_tasks"] = data["openActivityTasks"]
    else:
        out["open_activity_tasks"] = 0
    if "openDecisionTasks" in data:
        out["open_decision_tasks"] = data["openDecisionTasks"]
    else:
        out["open_decision_tasks"] = 0
    if "openTimers" in data:
        out["open_timers"] = data["openTimers"]
    else:
        out["open_timers"] = 0
    if "openChildWorkflowExecutions" in data:
        out["open_child_workflow_executions"] = data["openChildWorkflowExecutions"]
    else:
        out["open_child_workflow_executions"] = 0
    if "openLambdaFunctions" in data:
        out["open_lambda_functions"] = data["openLambdaFunctions"]
    else:
        out["open_lambda_functions"] = 0
    return out
