"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWorkflowsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.workflow_version_list


class ListWorkflowsResponse(TypedDict):
    workflow_version_list: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_version_list.WorkflowVersionList"
    ]
    """<p>A list of workflow build versions that match the request criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsResponse) -> dict:
    out: dict = {}
    if "workflow_version_list" in value:
        import aws_sdk_imagebuilder.types.workflow_version_list

        out["workflowVersionList"] = (
            aws_sdk_imagebuilder.types.workflow_version_list.serialize_json(
                value["workflow_version_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowsResponse:
    out: ListWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if "workflowVersionList" in data:
        import aws_sdk_imagebuilder.types.workflow_version_list

        out["workflow_version_list"] = (
            aws_sdk_imagebuilder.types.workflow_version_list.deserialize_json(
                data["workflowVersionList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
