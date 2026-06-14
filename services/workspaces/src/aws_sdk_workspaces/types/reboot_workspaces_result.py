"""Generated from Smithy shape ``com.amazonaws.workspaces#RebootWorkspacesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.failed_reboot_workspace_requests


class RebootWorkspacesResult(TypedDict):
    failed_requests: NotRequired[
        "aws_sdk_workspaces.types.failed_reboot_workspace_requests.FailedRebootWorkspaceRequests"
    ]
    """<p>Information about the WorkSpaces that could not be rebooted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import aws_sdk_workspaces.types.failed_reboot_workspace_requests

        out["FailedRequests"] = (
            aws_sdk_workspaces.types.failed_reboot_workspace_requests.serialize_aws_json_1_1(
                value["failed_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RebootWorkspacesResult:
    out: RebootWorkspacesResult = {}  # type: ignore[typeddict-item]
    if "FailedRequests" in data:
        import aws_sdk_workspaces.types.failed_reboot_workspace_requests

        out["failed_requests"] = (
            aws_sdk_workspaces.types.failed_reboot_workspace_requests.deserialize_aws_json_1_1(
                data["FailedRequests"]
            )
        )
    return out
