"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet

SubnetList: TypeAlias = list["aws_sdk_ec2.types.subnet.Subnet"]
