"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect


class CreateTransitGatewayConnectResult(TypedDict):
    transit_gateway_connect: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect.TransitGatewayConnect"
    ]
    """<p>Information about the Connect attachment.</p>"""
