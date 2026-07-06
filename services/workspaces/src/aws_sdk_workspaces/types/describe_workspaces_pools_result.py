"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspaces_pools


class DescribeWorkspacesPoolsResult(TypedDict, closed=True):
    workspaces_pools: NotRequired[
        "aws_sdk_workspaces.types.workspaces_pools.WorkspacesPools"
    ]
    """<p>Information about the WorkSpaces Pools.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsResult) -> dict:
    out: dict = {}
    if "workspaces_pools" in value:
        import aws_sdk_workspaces.types.workspaces_pools

        out["WorkspacesPools"] = (
            aws_sdk_workspaces.types.workspaces_pools.serialize_aws_json_1_1(
                value["workspaces_pools"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolsResult:
    out: DescribeWorkspacesPoolsResult = {}  # type: ignore[typeddict-item]
    if "WorkspacesPools" in data:
        import aws_sdk_workspaces.types.workspaces_pools

        out["workspaces_pools"] = (
            aws_sdk_workspaces.types.workspaces_pools.deserialize_aws_json_1_1(
                data["WorkspacesPools"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
