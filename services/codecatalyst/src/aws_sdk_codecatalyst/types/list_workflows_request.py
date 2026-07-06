"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListWorkflowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.workflow_sort_criteria_list


class ListWorkflowsRequest(TypedDict, closed=True):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""
    sort_by: NotRequired[
        "aws_sdk_codecatalyst.types.workflow_sort_criteria_list.WorkflowSortCriteriaList"
    ]
    """<p>Information used to sort the items in the returned list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_codecatalyst.types.workflow_sort_criteria_list

        out["sortBy"] = (
            aws_sdk_codecatalyst.types.workflow_sort_criteria_list.serialize_json(
                value["sort_by"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListWorkflowsRequest:
    out: ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import aws_sdk_codecatalyst.types.workflow_sort_criteria_list

        out["sort_by"] = (
            aws_sdk_codecatalyst.types.workflow_sort_criteria_list.deserialize_json(
                data["sortBy"]
            )
        )
    return out
