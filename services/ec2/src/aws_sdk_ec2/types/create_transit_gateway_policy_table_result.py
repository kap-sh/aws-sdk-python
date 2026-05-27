"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayPolicyTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table


class CreateTransitGatewayPolicyTableResult(TypedDict):
    transit_gateway_policy_table: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table.TransitGatewayPolicyTable"
    ]
    """<p>Describes the created transit gateway policy table.</p>"""
