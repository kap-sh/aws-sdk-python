"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_status_item

VolumeStatusList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_status_item.VolumeStatusItem"
]
