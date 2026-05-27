"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusAttachmentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_status_attachment_status

VolumeStatusAttachmentStatusList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_status_attachment_status.VolumeStatusAttachmentStatus"
]
