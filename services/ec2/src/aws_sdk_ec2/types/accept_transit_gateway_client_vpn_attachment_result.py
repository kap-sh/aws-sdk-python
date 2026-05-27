"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptTransitGatewayClientVpnAttachmentResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_client_vpn_attachment


class AcceptTransitGatewayClientVpnAttachmentResult(TypedDict):
    transit_gateway_client_vpn_attachment: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_client_vpn_attachment.TransitGatewayClientVpnAttachment"
    ]
    """<p>Information about the Transit Gateway Client VPN attachment.</p>"""
