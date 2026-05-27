"""Generated from Smithy shape ``com.amazonaws.ec2#DisableTransitGatewayRouteTablePropagationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_propagation


class DisableTransitGatewayRouteTablePropagationResult(TypedDict):
    propagation: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_propagation.TransitGatewayPropagation"
    ]
    """<p>Information about route propagation.</p>"""
