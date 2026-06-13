"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DisassociateVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.device_name
    import aws_sdk_workspaces_instances.types.disassociate_mode_enum
    import aws_sdk_workspaces_instances.types.volume_id
    import aws_sdk_workspaces_instances.types.workspace_instance_id


class DisassociateVolumeRequest(TypedDict):
    workspace_instance_id: (
        "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>WorkSpace Instance to detach volume from.</p>"""
    volume_id: "aws_sdk_workspaces_instances.types.volume_id.VolumeId"
    """<p>Volume to be detached.</p>"""
    device: NotRequired["aws_sdk_workspaces_instances.types.device_name.DeviceName"]
    """<p>Device path of volume to detach.</p>"""
    disassociate_mode: NotRequired[
        "aws_sdk_workspaces_instances.types.disassociate_mode_enum.DisassociateModeEnum"
    ]
    """<p>Mode for volume detachment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateVolumeRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    out["VolumeId"] = value["volume_id"]
    if "device" in value:
        out["Device"] = value["device"]
    if "disassociate_mode" in value:
        import aws_sdk_workspaces_instances.types.disassociate_mode_enum

        out["DisassociateMode"] = (
            aws_sdk_workspaces_instances.types.disassociate_mode_enum.serialize_aws_json_1_0(
                value["disassociate_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateVolumeRequest:
    out: DisassociateVolumeRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        raise DeserializationError(
            "DisassociateVolumeRequest.workspace_instance_id required"
        )
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    else:
        raise DeserializationError("DisassociateVolumeRequest.volume_id required")
    if "Device" in data:
        out["device"] = data["Device"]
    if "DisassociateMode" in data:
        import aws_sdk_workspaces_instances.types.disassociate_mode_enum

        out["disassociate_mode"] = (
            aws_sdk_workspaces_instances.types.disassociate_mode_enum.deserialize_aws_json_1_0(
                data["DisassociateMode"]
            )
        )
    return out
