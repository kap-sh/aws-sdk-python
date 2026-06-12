"""Generated from Smithy shape ``com.amazonaws.ssm#ParentStepDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_action_name
    import aws_sdk_ssm.types.integer
    import aws_sdk_ssm.types.string


class ParentStepDetails(TypedDict):
    step_execution_id: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The unique ID of a step execution.</p>"""
    step_name: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The name of the step.</p>"""
    action: NotRequired["aws_sdk_ssm.types.automation_action_name.AutomationActionName"]
    """<p>The name of the automation action.</p>"""
    iteration: NotRequired["aws_sdk_ssm.types.integer.Integer"]
    """<p>The current repetition of the loop represented by an integer.</p>"""
    iterator_value: NotRequired["aws_sdk_ssm.types.string.String"]
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
    if "StepExecutionId" in data:
        out["step_execution_id"] = data["StepExecutionId"]
    if "StepName" in data:
        out["step_name"] = data["StepName"]
    if "Action" in data:
        out["action"] = data["Action"]
    if "Iteration" in data:
        out["iteration"] = data["Iteration"]
    if "IteratorValue" in data:
        out["iterator_value"] = data["IteratorValue"]
    return out
