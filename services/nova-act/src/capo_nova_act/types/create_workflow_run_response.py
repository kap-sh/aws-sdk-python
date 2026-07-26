"""Generated from Smithy shape ``com.amazonaws.novaact#CreateWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_run_status


class CreateWorkflowRunResponse(TypedDict, closed=True):
    workflow_run_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier for the created workflow run.</p>"""
    status: "capo_nova_act.types.workflow_run_status.WorkflowRunStatus"
    """<p>The initial status of the workflow run after creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowRunResponse) -> dict:
    out: dict = {}
    out["workflowRunId"] = value["workflow_run_id"]
    import capo_nova_act.types.workflow_run_status

    out["status"] = capo_nova_act.types.workflow_run_status.serialize_json(
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
        import capo_nova_act.types.workflow_run_status

        out["status"] = capo_nova_act.types.workflow_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateWorkflowRunResponse.status required")
    return out
