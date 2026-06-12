"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.bundle_id
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.limit
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.user_name
    import aws_sdk_workspaces.types.workspace_id_list
    import aws_sdk_workspaces.types.workspace_name


class DescribeWorkspacesRequest(TypedDict):
    workspace_ids: NotRequired[
        "aws_sdk_workspaces.types.workspace_id_list.WorkspaceIdList"
    ]
    """<p>The identifiers of the WorkSpaces. You cannot combine this parameter with any other filter.</p> <p>Because the <a>CreateWorkspaces</a> operation is asynchronous, the identifier it returns is not immediately available. If you immediately call <a>DescribeWorkspaces</a> with this identifier, no information is returned.</p>"""
    directory_id: NotRequired["aws_sdk_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory. In addition, you can optionally specify a specific directory user (see <code>UserName</code>). You cannot combine this parameter with any other filter.</p>"""
    user_name: NotRequired["aws_sdk_workspaces.types.user_name.UserName"]
    """<p>The name of the directory user. You must specify this parameter with <code>DirectoryId</code>.</p>"""
    bundle_id: NotRequired["aws_sdk_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle. All WorkSpaces that are created from this bundle are retrieved. You cannot combine this parameter with any other filter.</p>"""
    limit: NotRequired["aws_sdk_workspaces.types.limit.Limit"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""
    workspace_name: NotRequired["aws_sdk_workspaces.types.workspace_name.WorkspaceName"]
    """<p>The name of the user-decoupled WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesRequest) -> dict:
    out: dict = {}
    if "workspace_ids" in value:
        import aws_sdk_workspaces.types.workspace_id_list

        out["WorkspaceIds"] = (
            aws_sdk_workspaces.types.workspace_id_list.serialize_aws_json_1_1(
                value["workspace_ids"]
            )
        )
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "workspace_name" in value:
        out["WorkspaceName"] = value["workspace_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesRequest:
    out: DescribeWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceIds" in data:
        import aws_sdk_workspaces.types.workspace_id_list

        out["workspace_ids"] = (
            aws_sdk_workspaces.types.workspace_id_list.deserialize_aws_json_1_1(
                data["WorkspaceIds"]
            )
        )
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WorkspaceName" in data:
        out["workspace_name"] = data["WorkspaceName"]
    return out
