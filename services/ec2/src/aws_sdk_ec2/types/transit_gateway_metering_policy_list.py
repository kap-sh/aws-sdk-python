"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy

TransitGatewayMeteringPolicyList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_metering_policy.TransitGatewayMeteringPolicy"
]
