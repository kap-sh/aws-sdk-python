"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BlockDeviceMappingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.device_name
    import aws_sdk_workspaces_instances.types.ebs_block_device
    import aws_sdk_workspaces_instances.types.virtual_name

class BlockDeviceMappingRequest(TypedDict):
    device_name: NotRequired["aws_sdk_workspaces_instances.types.device_name.DeviceName"]
    """<p>Name of the device for storage mapping.</p>"""
    ebs: NotRequired["aws_sdk_workspaces_instances.types.ebs_block_device.EbsBlockDevice"]
    """<p>EBS volume configuration for the device.</p>"""
    no_device: NotRequired["aws_sdk_workspaces_instances.types.device_name.DeviceName"]
    """<p>Indicates device should not be mapped.</p>"""
    virtual_name: NotRequired["aws_sdk_workspaces_instances.types.virtual_name.VirtualName"]
    """<p>Virtual device name for ephemeral storage.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlockDeviceMappingRequest) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "ebs" in value:
        import aws_sdk_workspaces_instances.types.ebs_block_device
        out["Ebs"] = aws_sdk_workspaces_instances.types.ebs_block_device.serialize_aws_json_1_0(value["ebs"])
    if "no_device" in value:
        out["NoDevice"] = value["no_device"]
    if "virtual_name" in value:
        out["VirtualName"] = value["virtual_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BlockDeviceMappingRequest:
    out: BlockDeviceMappingRequest = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "Ebs" in data:
        import aws_sdk_workspaces_instances.types.ebs_block_device
        out["ebs"] = aws_sdk_workspaces_instances.types.ebs_block_device.deserialize_aws_json_1_0(data["Ebs"])
    if "NoDevice" in data:
        out["no_device"] = data["NoDevice"]
    if "VirtualName" in data:
        out["virtual_name"] = data["VirtualName"]
    return out