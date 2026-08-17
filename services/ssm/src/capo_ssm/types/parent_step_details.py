"""Generated from Smithy shape ``com.amazonaws.ssm#ParentStepDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_action_name
    import capo_ssm.types.integer
    import capo_ssm.types.string


class ParentStepDetails(TypedDict, closed=True):
    step_execution_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The unique ID of a step execution.</p>"""
    step_name: NotRequired["capo_ssm.types.string.String"]
    """<p>The name of the step.</p>"""
    action: NotRequired["capo_ssm.types.automation_action_name.AutomationActionName"]
    """<p>The name of the automation action.</p>"""
    iteration: NotRequired["capo_ssm.types.integer.Integer"]
    """<p>The current repetition of the loop represented by an integer.</p>"""
    iterator_value: NotRequired["capo_ssm.types.string.String"]
    """<p>The current value of the specified iterator in the loop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParentStepDetails) -> dict:
    out: dict = {}
    if "step_execution_id" in value:
        out["StepExecutionId"] = value["step_execution_id"]
    if "step_name" in value:
        out["StepName"] = value["step_name"]
    if "action" in value:
        out["Action"] = value["action"]
    if "iteration" in value:
        out["Iteration"] = value["iteration"]
    if "iterator_value" in value:
        out["IteratorValue"] = value["iterator_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParentStepDetails:
    out: ParentStepDetails = {}  # type: ignore[typeddict-item]
    if data.get("StepExecutionId") is not None:
        out["step_execution_id"] = data["StepExecutionId"]
    if data.get("StepName") is not None:
        out["step_name"] = data["StepName"]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    if data.get("Iteration") is not None:
        out["iteration"] = data["Iteration"]
    if data.get("IteratorValue") is not None:
        out["iterator_value"] = data["IteratorValue"]
    return out
