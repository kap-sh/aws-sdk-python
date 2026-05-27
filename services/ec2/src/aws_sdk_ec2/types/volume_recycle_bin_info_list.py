"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeRecycleBinInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_recycle_bin_info

VolumeRecycleBinInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_recycle_bin_info.VolumeRecycleBinInfo"
]
