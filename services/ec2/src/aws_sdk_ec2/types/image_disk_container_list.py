"""Generated from Smithy shape ``com.amazonaws.ec2#ImageDiskContainerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_disk_container

ImageDiskContainerList: TypeAlias = list[
    "aws_sdk_ec2.types.image_disk_container.ImageDiskContainer"
]
