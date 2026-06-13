"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#RetryWorkflowStepResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.step_status


class RetryWorkflowStepResponse(TypedDict):
    step_group_id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the step.</p>"""
    status: NotRequired["aws_sdk_migrationhuborchestrator.types.step_status.StepStatus"]
    """<p>The status of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryWorkflowStepResponse) -> dict:
    out: dict = {}
    if "step_group_id" in value:
        out["stepGroupId"] = value["step_group_id"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> RetryWorkflowStepResponse:
    out: RetryWorkflowStepResponse = {}  # type: ignore[typeddict-item]
    if "stepGroupId" in data:
        out["step_group_id"] = data["stepGroupId"]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    return out
