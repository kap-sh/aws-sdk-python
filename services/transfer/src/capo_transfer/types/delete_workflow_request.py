"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.workflow_id


class DeleteWorkflowRequest(TypedDict, closed=True):
    workflow_id: "capo_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkflowRequest) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkflowRequest:
    out: DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    else:
        raise DeserializationError("DeleteWorkflowRequest.workflow_id required")
    return out
