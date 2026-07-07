"""Generated from Smithy shape ``com.amazonaws.workspaces#RebootWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.reboot_workspace_requests


class RebootWorkspacesRequest(TypedDict, closed=True):
    reboot_workspace_requests: (
        "aws_sdk_workspaces.types.reboot_workspace_requests.RebootWorkspaceRequests"
    )
    """<p>The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootWorkspacesRequest) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.reboot_workspace_requests

    out["RebootWorkspaceRequests"] = (
        aws_sdk_workspaces.types.reboot_workspace_requests.serialize_aws_json_1_1(
            value["reboot_workspace_requests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RebootWorkspacesRequest:
    out: RebootWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "RebootWorkspaceRequests" in data:
        import aws_sdk_workspaces.types.reboot_workspace_requests

        out["reboot_workspace_requests"] = (
            aws_sdk_workspaces.types.reboot_workspace_requests.deserialize_aws_json_1_1(
                data["RebootWorkspaceRequests"]
            )
        )
    else:
        raise DeserializationError(
            "RebootWorkspacesRequest.reboot_workspace_requests required"
        )
    return out
