"""Generated from Smithy shape ``com.amazonaws.novaact#CreateWorkflowRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_run_status


class CreateWorkflowRunResponse(TypedDict):
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier for the created workflow run.</p>"""
    status: "aws_sdk_nova_act.types.workflow_run_status.WorkflowRunStatus"
    """<p>The initial status of the workflow run after creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowRunResponse) -> dict:
    out: dict = {}
    out["workflowRunId"] = value["workflow_run_id"]
    import aws_sdk_nova_act.types.workflow_run_status

    out["status"] = aws_sdk_nova_act.types.workflow_run_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateWorkflowRunResponse:
    out: CreateWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "workflowRunId" in data:
        out["workflow_run_id"] = data["workflowRunId"]
    else:
        raise DeserializationError("CreateWorkflowRunResponse.workflow_run_id required")
    if "status" in data:
        import aws_sdk_nova_act.types.workflow_run_status

        out["status"] = aws_sdk_nova_act.types.workflow_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateWorkflowRunResponse.status required")
    return out
