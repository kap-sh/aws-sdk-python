"""Generated from Smithy shape ``com.amazonaws.omics#DeleteWorkflowVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_version_name


class DeleteWorkflowVersionRequest(TypedDict, closed=True):
    workflow_id: "aws_sdk_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID.</p>"""
    version_name: "aws_sdk_omics.types.workflow_version_name.WorkflowVersionName"
    """<p>The workflow version name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowVersionRequest:
    out: DeleteWorkflowVersionRequest = {}  # type: ignore[typeddict-item]
    return out
