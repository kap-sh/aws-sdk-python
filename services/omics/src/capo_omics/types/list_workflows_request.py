"""Generated from Smithy shape ``com.amazonaws.omics#ListWorkflowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.workflow_list_token
    import capo_omics.types.workflow_name
    import capo_omics.types.workflow_type


class ListWorkflowsRequest(TypedDict, closed=True):
    type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>Filter the list by workflow type.</p>"""
    name: NotRequired["capo_omics.types.workflow_name.WorkflowName"]
    """<p>Filter the list by workflow name.</p>"""
    starting_token: NotRequired[
        "capo_omics.types.workflow_list_token.WorkflowListToken"
    ]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of workflows to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkflowsRequest:
    out: ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
    return out
