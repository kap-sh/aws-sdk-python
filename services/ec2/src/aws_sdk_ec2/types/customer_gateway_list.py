"""Generated from Smithy shape ``com.amazonaws.ec2#CustomerGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway

CustomerGatewayList: TypeAlias = list[
    "aws_sdk_ec2.types.customer_gateway.CustomerGateway"
]
