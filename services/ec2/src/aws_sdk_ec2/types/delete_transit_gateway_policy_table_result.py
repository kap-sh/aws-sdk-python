"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayPolicyTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table


class DeleteTransitGatewayPolicyTableResult(TypedDict):
    transit_gateway_policy_table: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table.TransitGatewayPolicyTable"
    ]
    """<p>Provides details about the deleted transit gateway policy table.</p>"""
