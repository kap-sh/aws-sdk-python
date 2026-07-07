"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWorkflowBuildVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.restricted_integer
    import aws_sdk_imagebuilder.types.workflow_wildcard_version_arn


class ListWorkflowBuildVersionsRequest(TypedDict, closed=True):
    workflow_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_wildcard_version_arn.WorkflowWildcardVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow resource for which to get a list of build versions.</p>"""
    max_results: NotRequired[
        "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowBuildVersionsRequest) -> dict:
    out: dict = {}
    if "workflow_version_arn" in value:
        out["workflowVersionArn"] = value["workflow_version_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowBuildVersionsRequest:
    out: ListWorkflowBuildVersionsRequest = {}  # type: ignore[typeddict-item]
    if "workflowVersionArn" in data:
        out["workflow_version_arn"] = data["workflowVersionArn"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
