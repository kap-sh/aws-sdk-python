"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockOfferingSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_offering

CapacityBlockOfferingSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_block_offering.CapacityBlockOffering"
]
