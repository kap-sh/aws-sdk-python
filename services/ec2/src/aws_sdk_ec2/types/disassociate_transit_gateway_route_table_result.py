"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTransitGatewayRouteTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_association


class DisassociateTransitGatewayRouteTableResult(TypedDict):
    association: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_association.TransitGatewayAssociation"
    ]
    """<p>Information about the association.</p>"""
