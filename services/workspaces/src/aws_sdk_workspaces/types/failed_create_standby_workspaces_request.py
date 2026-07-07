"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedCreateStandbyWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.description
    import aws_sdk_workspaces.types.standby_workspace
    import aws_sdk_workspaces.types.workspace_error_code


class FailedCreateStandbyWorkspacesRequest(TypedDict, closed=True):
    standby_workspace_request: NotRequired[
        "aws_sdk_workspaces.types.standby_workspace.StandbyWorkspace"
    ]
    """<p>Information about the standby WorkSpace that could not be created.</p>"""
    error_code: NotRequired[
        "aws_sdk_workspaces.types.workspace_error_code.WorkspaceErrorCode"
    ]
    """<p>The error code that is returned if the standby WorkSpace could not be created.</p>"""
    error_message: NotRequired["aws_sdk_workspaces.types.description.Description"]
    """<p>The text of the error message that is returned if the standby WorkSpace could not be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedCreateStandbyWorkspacesRequest) -> dict:
    out: dict = {}
    if "standby_workspace_request" in value:
        import aws_sdk_workspaces.types.standby_workspace

        out["StandbyWorkspaceRequest"] = (
            aws_sdk_workspaces.types.standby_workspace.serialize_aws_json_1_1(
                value["standby_workspace_request"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedCreateStandbyWorkspacesRequest:
    out: FailedCreateStandbyWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "StandbyWorkspaceRequest" in data:
        import aws_sdk_workspaces.types.standby_workspace

        out["standby_workspace_request"] = (
            aws_sdk_workspaces.types.standby_workspace.deserialize_aws_json_1_1(
                data["StandbyWorkspaceRequest"]
            )
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
