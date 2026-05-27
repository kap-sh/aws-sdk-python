"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_image

DiskImageList: TypeAlias = list["aws_sdk_ec2.types.disk_image.DiskImage"]
