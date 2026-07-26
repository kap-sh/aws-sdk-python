"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#GetWorkspaceInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_instances.types.workspace_instance_id


class GetWorkspaceInstanceRequest(TypedDict, closed=True):
    workspace_instance_id: (
        "capo_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>Unique identifier of the WorkSpace Instance to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkspaceInstanceRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkspaceInstanceRequest:
    out: GetWorkspaceInstanceRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        raise DeserializationError(
            "GetWorkspaceInstanceRequest.workspace_instance_id required"
        )
    return out
