"""Generated from Smithy shape ``com.amazonaws.omics#DeleteWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.workflow_id


class DeleteWorkflowRequest(TypedDict, closed=True):
    id: "capo_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowRequest:
    out: DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
