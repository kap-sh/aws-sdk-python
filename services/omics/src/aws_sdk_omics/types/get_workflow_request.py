"""Generated from Smithy shape ``com.amazonaws.omics#GetWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.workflow_export_list
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_owner_id
    import aws_sdk_omics.types.workflow_type


class GetWorkflowRequest(TypedDict, closed=True):
    id: "aws_sdk_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID.</p>"""
    type: NotRequired["aws_sdk_omics.types.workflow_type.WorkflowType"]
    """<p>The workflow's type.</p>"""
    export: NotRequired["aws_sdk_omics.types.workflow_export_list.WorkflowExportList"]
    """<p>The export format for the workflow.</p>"""
    workflow_owner_id: NotRequired[
        "aws_sdk_omics.types.workflow_owner_id.WorkflowOwnerId"
    ]
    """<p>The ID of the workflow owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowRequest:
    out: GetWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
