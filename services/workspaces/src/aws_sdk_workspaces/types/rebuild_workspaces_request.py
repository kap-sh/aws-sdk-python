"""Generated from Smithy shape ``com.amazonaws.workspaces#RebuildWorkspacesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.rebuild_workspace_requests


class RebuildWorkspacesRequest(TypedDict):
    rebuild_workspace_requests: (
        "aws_sdk_workspaces.types.rebuild_workspace_requests.RebuildWorkspaceRequests"
    )
    """<p>The WorkSpace to rebuild. You can specify a single WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebuildWorkspacesRequest) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.rebuild_workspace_requests

    out["RebuildWorkspaceRequests"] = (
        aws_sdk_workspaces.types.rebuild_workspace_requests.serialize_aws_json_1_1(
            value["rebuild_workspace_requests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RebuildWorkspacesRequest:
    out: RebuildWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "RebuildWorkspaceRequests" in data:
        import aws_sdk_workspaces.types.rebuild_workspace_requests

        out["rebuild_workspace_requests"] = (
            aws_sdk_workspaces.types.rebuild_workspace_requests.deserialize_aws_json_1_1(
                data["RebuildWorkspaceRequests"]
            )
        )
    else:
        raise DeserializationError(
            "RebuildWorkspacesRequest.rebuild_workspace_requests required"
        )
    return out
