"""Generated from Smithy shape ``com.amazonaws.ec2#BlockDeviceMappingResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_device_mapping_response

BlockDeviceMappingResponseList: TypeAlias = list[
    "aws_sdk_ec2.types.block_device_mapping_response.BlockDeviceMappingResponse"
]
