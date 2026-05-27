"""Generated from Smithy shape ``com.amazonaws.ec2#CarrierGatewayIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway_id

CarrierGatewayIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.carrier_gateway_id.CarrierGatewayId"
]
