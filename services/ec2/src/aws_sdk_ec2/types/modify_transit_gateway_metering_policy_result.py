"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayMeteringPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy


class ModifyTransitGatewayMeteringPolicyResult(TypedDict):
    transit_gateway_metering_policy: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy.TransitGatewayMeteringPolicy"
    ]
    """<p>Information about the modified transit gateway metering policy.</p>"""
