"""Generated from Smithy shape ``com.amazonaws.novaact#DeleteWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.workflow_run_status


class DeleteWorkflowRunResponse(TypedDict, closed=True):
    status: "capo_nova_act.types.workflow_run_status.WorkflowRunStatus"
    """<p>The status of the workflow run after deletion request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowRunResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.workflow_run_status

    out["status"] = capo_nova_act.types.workflow_run_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteWorkflowRunResponse:
    out: DeleteWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_nova_act.types.workflow_run_status

        out["status"] = capo_nova_act.types.workflow_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteWorkflowRunResponse.status required")
    return out
