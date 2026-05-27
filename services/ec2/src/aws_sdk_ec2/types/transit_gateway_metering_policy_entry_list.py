"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy_entry

TransitGatewayMeteringPolicyEntryList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_metering_policy_entry.TransitGatewayMeteringPolicyEntry"
]
