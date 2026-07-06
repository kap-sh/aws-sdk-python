"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedWorkspaceChangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.description
    import aws_sdk_workspaces.types.error_type
    import aws_sdk_workspaces.types.workspace_id


class FailedWorkspaceChangeRequest(TypedDict, closed=True):
    workspace_id: NotRequired["aws_sdk_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the WorkSpace.</p>"""
    error_code: NotRequired["aws_sdk_workspaces.types.error_type.ErrorType"]
    """<p>The error code that is returned if the WorkSpace cannot be rebooted.</p>"""
    error_message: NotRequired["aws_sdk_workspaces.types.description.Description"]
    """<p>The text of the error message that is returned if the WorkSpace cannot be rebooted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedWorkspaceChangeRequest) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedWorkspaceChangeRequest:
    out: FailedWorkspaceChangeRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
