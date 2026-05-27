"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTransitGatewayPolicyTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table_association


class AssociateTransitGatewayPolicyTableResult(TypedDict):
    association: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_association.TransitGatewayPolicyTableAssociation"
    ]
    """<p>Describes the association of a transit gateway and a transit gateway policy table.</p>"""
