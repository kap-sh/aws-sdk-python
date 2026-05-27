"""Generated from Smithy shape ``com.amazonaws.ec2#MediaDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.media_device_info

MediaDeviceInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.media_device_info.MediaDeviceInfo"
]
