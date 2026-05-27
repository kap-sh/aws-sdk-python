"""Generated from Smithy shape ``com.amazonaws.ec2#PeeringAttachmentStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PeeringAttachmentStatus(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message, if applicable.</p>"""
