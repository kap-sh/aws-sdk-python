"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWorkflowBuildVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.workflow_summary_list


class ListWorkflowBuildVersionsResponse(TypedDict, closed=True):
    workflow_summary_list: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_summary_list.WorkflowSummaryList"
    ]
    """<p>A list that contains metadata for the workflow builds that have run for the workflow resource specified in the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowBuildVersionsResponse) -> dict:
    out: dict = {}
    if "workflow_summary_list" in value:
        import aws_sdk_imagebuilder.types.workflow_summary_list

        out["workflowSummaryList"] = (
            aws_sdk_imagebuilder.types.workflow_summary_list.serialize_json(
                value["workflow_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowBuildVersionsResponse:
    out: ListWorkflowBuildVersionsResponse = {}  # type: ignore[typeddict-item]
    if "workflowSummaryList" in data:
        import aws_sdk_imagebuilder.types.workflow_summary_list

        out["workflow_summary_list"] = (
            aws_sdk_imagebuilder.types.workflow_summary_list.deserialize_json(
                data["workflowSummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
