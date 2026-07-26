"""Generated from Smithy shape ``com.amazonaws.omics#GetWorkflowVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.workflow_export_list
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_owner_id
    import capo_omics.types.workflow_type
    import capo_omics.types.workflow_version_name


class GetWorkflowVersionRequest(TypedDict, closed=True):
    workflow_id: "capo_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID. The <code>workflowId</code> is not the UUID.</p>"""
    version_name: "capo_omics.types.workflow_version_name.WorkflowVersionName"
    """<p>The workflow version name.</p>"""
    type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>The workflow's type. </p>"""
    export: NotRequired["capo_omics.types.workflow_export_list.WorkflowExportList"]
    """<p>The export format for the workflow.</p>"""
    workflow_owner_id: NotRequired["capo_omics.types.workflow_owner_id.WorkflowOwnerId"]
    """<p>The 12-digit account ID of the workflow owner. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowVersionRequest:
    out: GetWorkflowVersionRequest = {}  # type: ignore[typeddict-item]
    return out
