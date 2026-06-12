"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AssociateVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces_instances.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.device_name
    import aws_sdk_workspaces_instances.types.volume_id
    import aws_sdk_workspaces_instances.types.workspace_instance_id

class AssociateVolumeRequest(TypedDict):
    workspace_instance_id: "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    """<p>WorkSpace Instance to attach volume to.</p>"""
    volume_id: "aws_sdk_workspaces_instances.types.volume_id.VolumeId"
    """<p>Volume to be attached.</p>"""
    device: "aws_sdk_workspaces_instances.types.device_name.DeviceName"
    """<p>Device path for volume attachment.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateVolumeRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    out["VolumeId"] = value["volume_id"]
    out["Device"] = value["device"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateVolumeRequest:
    out: AssociateVolumeRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        raise DeserializationError("AssociateVolumeRequest.workspace_instance_id required")
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    else:
        raise DeserializationError("AssociateVolumeRequest.volume_id required")
    if "Device" in data:
        out["device"] = data["Device"]
    else:
        raise DeserializationError("AssociateVolumeRequest.device required")
    return out