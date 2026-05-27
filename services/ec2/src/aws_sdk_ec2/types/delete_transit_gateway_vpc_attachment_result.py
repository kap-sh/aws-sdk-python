"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayVpcAttachmentResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_vpc_attachment


class DeleteTransitGatewayVpcAttachmentResult(TypedDict):
    transit_gateway_vpc_attachment: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_vpc_attachment.TransitGatewayVpcAttachment"
    ]
    """<p>Information about the deleted VPC attachment.</p>"""
