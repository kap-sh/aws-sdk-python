"""Generated from Smithy shape ``com.amazonaws.workspaces#StartWorkspacesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.start_workspace_requests


class StartWorkspacesRequest(TypedDict):
    start_workspace_requests: (
        "aws_sdk_workspaces.types.start_workspace_requests.StartWorkspaceRequests"
    )
    """<p>The WorkSpaces to start. You can specify up to 25 WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkspacesRequest) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.start_workspace_requests

    out["StartWorkspaceRequests"] = (
        aws_sdk_workspaces.types.start_workspace_requests.serialize_aws_json_1_1(
            value["start_workspace_requests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWorkspacesRequest:
    out: StartWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "StartWorkspaceRequests" in data:
        import aws_sdk_workspaces.types.start_workspace_requests

        out["start_workspace_requests"] = (
            aws_sdk_workspaces.types.start_workspace_requests.deserialize_aws_json_1_1(
                data["StartWorkspaceRequests"]
            )
        )
    else:
        raise DeserializationError(
            "StartWorkspacesRequest.start_workspace_requests required"
        )
    return out
