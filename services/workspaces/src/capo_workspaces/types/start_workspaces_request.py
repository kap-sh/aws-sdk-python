"""Generated from Smithy shape ``com.amazonaws.workspaces#StartWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.start_workspace_requests


class StartWorkspacesRequest(TypedDict, closed=True):
    start_workspace_requests: (
        "capo_workspaces.types.start_workspace_requests.StartWorkspaceRequests"
    )
    """<p>The WorkSpaces to start. You can specify up to 25 WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkspacesRequest) -> dict:
    out: dict = {}
    import capo_workspaces.types.start_workspace_requests

    out["StartWorkspaceRequests"] = (
        capo_workspaces.types.start_workspace_requests.serialize_aws_json_1_1(
            value["start_workspace_requests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWorkspacesRequest:
    out: StartWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "StartWorkspaceRequests" in data:
        import capo_workspaces.types.start_workspace_requests

        out["start_workspace_requests"] = (
            capo_workspaces.types.start_workspace_requests.deserialize_aws_json_1_1(
                data["StartWorkspaceRequests"]
            )
        )
    else:
        raise DeserializationError(
            "StartWorkspacesRequest.start_workspace_requests required"
        )
    return out
