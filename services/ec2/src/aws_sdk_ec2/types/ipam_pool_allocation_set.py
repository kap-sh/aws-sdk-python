"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolAllocationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_allocation

IpamPoolAllocationSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_pool_allocation.IpamPoolAllocation"
]
