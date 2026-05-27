"""Generated from Smithy shape ``com.amazonaws.ec2#BlockDeviceMappingRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_device_mapping

BlockDeviceMappingRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.block_device_mapping.BlockDeviceMapping"
]
