"""Generated from Smithy shape ``com.amazonaws.ec2#VpcAttachment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attachment_status
    import aws_sdk_ec2.types.string


class VpcAttachment(TypedDict):
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    state: NotRequired["aws_sdk_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The current state of the attachment.</p>"""
