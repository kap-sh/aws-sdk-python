"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAllocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_allocation

CapacityAllocations: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_allocation.CapacityAllocation"
]
