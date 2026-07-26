"""Generated from Smithy shape ``com.amazonaws.omics#ListWorkflowVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_owner_id
    import capo_omics.types.workflow_type
    import capo_omics.types.workflow_version_list_token


class ListWorkflowVersionsRequest(TypedDict, closed=True):
    workflow_id: "capo_omics.types.workflow_id.WorkflowId"
    """<p>The workflow's ID. The <code>workflowId</code> is not the UUID.</p>"""
    type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>The workflow type.</p>"""
    workflow_owner_id: NotRequired["capo_omics.types.workflow_owner_id.WorkflowOwnerId"]
    """<p>The 12-digit account ID of the workflow owner. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>"""
    starting_token: NotRequired[
        "capo_omics.types.workflow_version_list_token.WorkflowVersionListToken"
    ]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of workflows to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkflowVersionsRequest:
    out: ListWorkflowVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
