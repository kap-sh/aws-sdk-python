"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMeteringPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy


class CreateTransitGatewayMeteringPolicyResult(TypedDict):
    transit_gateway_metering_policy: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy.TransitGatewayMeteringPolicy"
    ]
    """<p>Information about the created transit gateway metering policy.</p>"""
