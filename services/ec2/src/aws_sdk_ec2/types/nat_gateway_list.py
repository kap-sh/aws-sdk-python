"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway

NatGatewayList: TypeAlias = list["aws_sdk_ec2.types.nat_gateway.NatGateway"]
