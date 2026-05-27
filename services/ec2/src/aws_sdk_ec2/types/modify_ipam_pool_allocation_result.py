"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPoolAllocationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_allocation


class ModifyIpamPoolAllocationResult(TypedDict):
    ipam_pool_allocation: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation.IpamPoolAllocation"
    ]
    """<p>The modified IPAM pool allocation.</p>"""
