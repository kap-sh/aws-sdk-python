"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway_id

NatGatewayIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.nat_gateway_id.NatGatewayId"
]
