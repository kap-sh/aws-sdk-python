"""Generated from Smithy shape ``com.amazonaws.ec2#ImageRecycleBinInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_recycle_bin_info

ImageRecycleBinInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.image_recycle_bin_info.ImageRecycleBinInfo"
]
