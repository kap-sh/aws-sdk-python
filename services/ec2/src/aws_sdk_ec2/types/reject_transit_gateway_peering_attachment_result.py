"""Generated from Smithy shape ``com.amazonaws.ec2#RejectTransitGatewayPeeringAttachmentResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_peering_attachment


class RejectTransitGatewayPeeringAttachmentResult(TypedDict):
    transit_gateway_peering_attachment: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_peering_attachment.TransitGatewayPeeringAttachment"
    ]
    """<p>The transit gateway peering attachment.</p>"""
