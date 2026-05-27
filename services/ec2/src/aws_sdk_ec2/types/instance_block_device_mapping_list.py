"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBlockDeviceMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_block_device_mapping

InstanceBlockDeviceMappingList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_block_device_mapping.InstanceBlockDeviceMapping"
]
