"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6RangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_range

Ipv6RangeList: TypeAlias = list["aws_sdk_ec2.types.ipv6_range.Ipv6Range"]
