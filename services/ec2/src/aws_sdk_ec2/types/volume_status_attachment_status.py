"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusAttachmentStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class VolumeStatusAttachmentStatus(TypedDict):
    io_performance: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum IOPS supported by the attached instance.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the attached instance.</p>"""
