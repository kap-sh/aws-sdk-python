"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway

TransitGatewayList: TypeAlias = list["aws_sdk_ec2.types.transit_gateway.TransitGateway"]
