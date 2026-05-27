"""Generated from Smithy shape ``com.amazonaws.ec2#IpRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_range

IpRangeList: TypeAlias = list["aws_sdk_ec2.types.ip_range.IpRange"]
