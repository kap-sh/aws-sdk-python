"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayMeteringPolicyEntryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy_entry


class DeleteTransitGatewayMeteringPolicyEntryResult(TypedDict):
    transit_gateway_metering_policy_entry: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_entry.TransitGatewayMeteringPolicyEntry"
    ]
    """<p>Information about the deleted transit gateway metering policy entry.</p>"""
