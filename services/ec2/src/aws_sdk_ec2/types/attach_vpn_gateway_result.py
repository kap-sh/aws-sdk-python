"""Generated from Smithy shape ``com.amazonaws.ec2#AttachVpnGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_attachment


class AttachVpnGatewayResult(TypedDict):
    vpc_attachment: NotRequired["aws_sdk_ec2.types.vpc_attachment.VpcAttachment"]
    """<p>Information about the attachment.</p>"""
