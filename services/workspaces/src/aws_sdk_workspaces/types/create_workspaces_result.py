"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.failed_create_workspace_requests
    import aws_sdk_workspaces.types.workspace_list


class CreateWorkspacesResult(TypedDict, closed=True):
    failed_requests: NotRequired[
        "aws_sdk_workspaces.types.failed_create_workspace_requests.FailedCreateWorkspaceRequests"
    ]
    """<p>Information about the WorkSpaces that could not be created.</p>"""
    pending_requests: NotRequired[
        "aws_sdk_workspaces.types.workspace_list.WorkspaceList"
    ]
    """<p>Information about the WorkSpaces that were created.</p> <p>Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call <a>DescribeWorkspaces</a> before the WorkSpace is created, the information returned can be incomplete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import aws_sdk_workspaces.types.failed_create_workspace_requests

        out["FailedRequests"] = (
            aws_sdk_workspaces.types.failed_create_workspace_requests.serialize_aws_json_1_1(
                value["failed_requests"]
            )
        )
    if "pending_requests" in value:
        import aws_sdk_workspaces.types.workspace_list

        out["PendingRequests"] = (
            aws_sdk_workspaces.types.workspace_list.serialize_aws_json_1_1(
                value["pending_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspacesResult:
    out: CreateWorkspacesResult = {}  # type: ignore[typeddict-item]
    if "FailedRequests" in data:
        import aws_sdk_workspaces.types.failed_create_workspace_requests

        out["failed_requests"] = (
            aws_sdk_workspaces.types.failed_create_workspace_requests.deserialize_aws_json_1_1(
                data["FailedRequests"]
            )
        )
    if "PendingRequests" in data:
        import aws_sdk_workspaces.types.workspace_list

        out["pending_requests"] = (
            aws_sdk_workspaces.types.workspace_list.deserialize_aws_json_1_1(
                data["PendingRequests"]
            )
        )
    return out
