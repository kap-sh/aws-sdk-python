"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DeleteWorkspaceInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.workspace_instance_id


class DeleteWorkspaceInstanceRequest(TypedDict):
    workspace_instance_id: (
        "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>Unique identifier of the WorkSpaces Instance targeted for deletion.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteWorkspaceInstanceRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteWorkspaceInstanceRequest:
    out: DeleteWorkspaceInstanceRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        raise DeserializationError(
            "DeleteWorkspaceInstanceRequest.workspace_instance_id required"
        )
    return out
