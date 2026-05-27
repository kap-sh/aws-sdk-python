"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway_address

NatGatewayAddressList: TypeAlias = list[
    "aws_sdk_ec2.types.nat_gateway_address.NatGatewayAddress"
]
