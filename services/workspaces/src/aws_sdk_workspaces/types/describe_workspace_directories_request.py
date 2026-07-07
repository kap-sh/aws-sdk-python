"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.describe_workspace_directories_filter_list
    import aws_sdk_workspaces.types.directory_id_list
    import aws_sdk_workspaces.types.limit
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspace_directory_name_list


class DescribeWorkspaceDirectoriesRequest(TypedDict, closed=True):
    directory_ids: NotRequired[
        "aws_sdk_workspaces.types.directory_id_list.DirectoryIdList"
    ]
    """<p>The identifiers of the directories. If the value is null, all directories are retrieved.</p>"""
    workspace_directory_names: NotRequired[
        "aws_sdk_workspaces.types.workspace_directory_name_list.WorkspaceDirectoryNameList"
    ]
    """<p>The names of the WorkSpace directories.</p>"""
    limit: NotRequired["aws_sdk_workspaces.types.limit.Limit"]
    """<p>The maximum number of directories to return.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""
    filters: NotRequired[
        "aws_sdk_workspaces.types.describe_workspace_directories_filter_list.DescribeWorkspaceDirectoriesFilterList"
    ]
    """<p>The filter condition for the WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesRequest) -> dict:
    out: dict = {}
    if "directory_ids" in value:
        import aws_sdk_workspaces.types.directory_id_list

        out["DirectoryIds"] = (
            aws_sdk_workspaces.types.directory_id_list.serialize_aws_json_1_1(
                value["directory_ids"]
            )
        )
    if "workspace_directory_names" in value:
        import aws_sdk_workspaces.types.workspace_directory_name_list

        out["WorkspaceDirectoryNames"] = (
            aws_sdk_workspaces.types.workspace_directory_name_list.serialize_aws_json_1_1(
                value["workspace_directory_names"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_workspaces.types.describe_workspace_directories_filter_list

        out["Filters"] = (
            aws_sdk_workspaces.types.describe_workspace_directories_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceDirectoriesRequest:
    out: DescribeWorkspaceDirectoriesRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryIds" in data:
        import aws_sdk_workspaces.types.directory_id_list

        out["directory_ids"] = (
            aws_sdk_workspaces.types.directory_id_list.deserialize_aws_json_1_1(
                data["DirectoryIds"]
            )
        )
    if "WorkspaceDirectoryNames" in data:
        import aws_sdk_workspaces.types.workspace_directory_name_list

        out["workspace_directory_names"] = (
            aws_sdk_workspaces.types.workspace_directory_name_list.deserialize_aws_json_1_1(
                data["WorkspaceDirectoryNames"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_workspaces.types.describe_workspace_directories_filter_list

        out["filters"] = (
            aws_sdk_workspaces.types.describe_workspace_directories_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
