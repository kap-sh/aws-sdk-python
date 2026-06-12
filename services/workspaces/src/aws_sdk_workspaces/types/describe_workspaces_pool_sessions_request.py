"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolSessionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.limit50
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspaces_pool_id
    import aws_sdk_workspaces.types.workspaces_pool_user_id


class DescribeWorkspacesPoolSessionsRequest(TypedDict):
    pool_id: "aws_sdk_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the pool.</p>"""
    user_id: NotRequired[
        "aws_sdk_workspaces.types.workspaces_pool_user_id.WorkspacesPoolUserId"
    ]
    """<p>The identifier of the user.</p>"""
    limit: NotRequired["aws_sdk_workspaces.types.limit50.Limit50"]
    """<p>The maximum size of each page of results. The default value is 20 and the maximum value is 50.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolSessionsRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolSessionsRequest:
    out: DescribeWorkspacesPoolSessionsRequest = {}  # type: ignore[typeddict-item]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError(
            "DescribeWorkspacesPoolSessionsRequest.pool_id required"
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
