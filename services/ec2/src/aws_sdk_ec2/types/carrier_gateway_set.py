"""Generated from Smithy shape ``com.amazonaws.ec2#CarrierGatewaySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway

CarrierGatewaySet: TypeAlias = list["aws_sdk_ec2.types.carrier_gateway.CarrierGateway"]
