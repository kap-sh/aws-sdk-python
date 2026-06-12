"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BlockDeviceMappings``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.block_device_mapping_request

BlockDeviceMappings: TypeAlias = list["aws_sdk_workspaces_instances.types.block_device_mapping_request.BlockDeviceMappingRequest"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlockDeviceMappings) -> list:
    import aws_sdk_workspaces_instances.types.block_device_mapping_request
    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_instances.types.block_device_mapping_request.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BlockDeviceMappings:
    import aws_sdk_workspaces_instances.types.block_device_mapping_request
    out: BlockDeviceMappings = []
    for item in data:
        out.append(aws_sdk_workspaces_instances.types.block_device_mapping_request.deserialize_aws_json_1_0(item))
    return out