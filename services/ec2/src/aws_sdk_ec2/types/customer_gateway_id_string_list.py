"""Generated from Smithy shape ``com.amazonaws.ec2#CustomerGatewayIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway_id

CustomerGatewayIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.customer_gateway_id.CustomerGatewayId"
]
