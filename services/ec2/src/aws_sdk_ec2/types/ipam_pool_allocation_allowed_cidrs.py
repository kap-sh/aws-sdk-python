"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolAllocationAllowedCidrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

IpamPoolAllocationAllowedCidrs: TypeAlias = list["aws_sdk_ec2.types.string.String"]
