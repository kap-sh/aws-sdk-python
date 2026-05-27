"""Generated from Smithy shape ``com.amazonaws.ec2#PortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port_range

PortRangeList: TypeAlias = list["aws_sdk_ec2.types.port_range.PortRange"]
