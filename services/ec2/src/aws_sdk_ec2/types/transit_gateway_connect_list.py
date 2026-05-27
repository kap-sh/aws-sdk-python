"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect

TransitGatewayConnectList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_connect.TransitGatewayConnect"
]
