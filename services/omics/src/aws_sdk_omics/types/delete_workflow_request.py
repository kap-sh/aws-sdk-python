"""Generated from Smithy shape ``com.amazonaws.omics#DeleteWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.workflow_id


class DeleteWorkflowRequest(TypedDict):
    id: "aws_sdk_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowRequest:
    out: DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
