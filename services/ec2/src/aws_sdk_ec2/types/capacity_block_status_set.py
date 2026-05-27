"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_status

CapacityBlockStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_block_status.CapacityBlockStatus"
]
