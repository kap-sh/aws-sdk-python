"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesConnectionStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspace_connection_status_list


class DescribeWorkspacesConnectionStatusResult(TypedDict, closed=True):
    workspaces_connection_status: NotRequired[
        "aws_sdk_workspaces.types.workspace_connection_status_list.WorkspaceConnectionStatusList"
    ]
    """<p>Information about the connection status of the WorkSpace.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesConnectionStatusResult) -> dict:
    out: dict = {}
    if "workspaces_connection_status" in value:
        import aws_sdk_workspaces.types.workspace_connection_status_list

        out["WorkspacesConnectionStatus"] = (
            aws_sdk_workspaces.types.workspace_connection_status_list.serialize_aws_json_1_1(
                value["workspaces_connection_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesConnectionStatusResult:
    out: DescribeWorkspacesConnectionStatusResult = {}  # type: ignore[typeddict-item]
    if "WorkspacesConnectionStatus" in data:
        import aws_sdk_workspaces.types.workspace_connection_status_list

        out["workspaces_connection_status"] = (
            aws_sdk_workspaces.types.workspace_connection_status_list.deserialize_aws_json_1_1(
                data["WorkspacesConnectionStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
