"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceImagePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.limit
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspace_image_id


class DescribeWorkspaceImagePermissionsRequest(TypedDict):
    image_id: "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the image.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_workspaces.types.limit.Limit"]
    """<p>The maximum number of items to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceImagePermissionsRequest) -> dict:
    out: dict = {}
    out["ImageId"] = value["image_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceImagePermissionsRequest:
    out: DescribeWorkspaceImagePermissionsRequest = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    else:
        raise DeserializationError(
            "DescribeWorkspaceImagePermissionsRequest.image_id required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
