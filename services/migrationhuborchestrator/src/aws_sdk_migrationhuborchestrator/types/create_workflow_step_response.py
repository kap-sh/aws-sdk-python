"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateWorkflowStepResponse``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CreateWorkflowStepResponse(TypedDict):
    id: NotRequired["str"]
    """<p>The ID of the step.</p>"""
    step_group_id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowStepResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "step_group_id" in value:
        out["stepGroupId"] = value["step_group_id"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowStepResponse:
    out: CreateWorkflowStepResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "stepGroupId" in data:
        out["step_group_id"] = data["stepGroupId"]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "name" in data:
        out["name"] = data["name"]
    return out
