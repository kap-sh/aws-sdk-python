"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTransitGatewayPolicyTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table_association


class DisassociateTransitGatewayPolicyTableResult(TypedDict):
    association: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_association.TransitGatewayPolicyTableAssociation"
    ]
    """<p>Returns details about the transit gateway policy table disassociation.</p>"""
