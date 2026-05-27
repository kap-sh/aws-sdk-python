"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network

SecondaryNetworkList: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_network.SecondaryNetwork"
]
