"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGatewayAttachment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attachment_status
    import aws_sdk_ec2.types.string


class InternetGatewayAttachment(TypedDict):
    state: NotRequired["aws_sdk_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The current state of the attachment. For an internet gateway, the state is <code>available</code> when attached to a VPC; otherwise, this value is not returned.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
