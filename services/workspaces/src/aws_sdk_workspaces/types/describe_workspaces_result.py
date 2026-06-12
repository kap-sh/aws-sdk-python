"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspace_list


class DescribeWorkspacesResult(TypedDict):
    workspaces: NotRequired["aws_sdk_workspaces.types.workspace_list.WorkspaceList"]
    """<p>Information about the WorkSpaces.</p> <p>Because <a>CreateWorkspaces</a> is an asynchronous operation, some of the returned information could be incomplete.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesResult) -> dict:
    out: dict = {}
    if "workspaces" in value:
        import aws_sdk_workspaces.types.workspace_list

        out["Workspaces"] = (
            aws_sdk_workspaces.types.workspace_list.serialize_aws_json_1_1(
                value["workspaces"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesResult:
    out: DescribeWorkspacesResult = {}  # type: ignore[typeddict-item]
    if "Workspaces" in data:
        import aws_sdk_workspaces.types.workspace_list

        out["workspaces"] = (
            aws_sdk_workspaces.types.workspace_list.deserialize_aws_json_1_1(
                data["Workspaces"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
