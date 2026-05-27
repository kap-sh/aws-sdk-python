"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block

CapacityBlockSet: TypeAlias = list["aws_sdk_ec2.types.capacity_block.CapacityBlock"]
