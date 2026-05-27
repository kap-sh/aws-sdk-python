"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id

TransitGatewayMeteringPolicyIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
]
