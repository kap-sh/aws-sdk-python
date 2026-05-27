"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_subnet

SecondarySubnetList: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_subnet.SecondarySubnet"
]
