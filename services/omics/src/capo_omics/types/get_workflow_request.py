"""Generated from Smithy shape ``com.amazonaws.omics#GetWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.workflow_export_list
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_owner_id
    import capo_omics.types.workflow_type


class GetWorkflowRequest(TypedDict, closed=True):
    id: "capo_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID.</p>"""
    type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>The workflow's type.</p>"""
    export: NotRequired["capo_omics.types.workflow_export_list.WorkflowExportList"]
    """<p>The export format for the workflow.</p>"""
    workflow_owner_id: NotRequired["capo_omics.types.workflow_owner_id.WorkflowOwnerId"]
    """<p>The ID of the workflow owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowRequest:
    out: GetWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
