"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_attachment

VolumeAttachmentList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_attachment.VolumeAttachment"
]
