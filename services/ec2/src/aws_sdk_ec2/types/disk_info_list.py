"""Generated from Smithy shape ``com.amazonaws.ec2#DiskInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_info

DiskInfoList: TypeAlias = list["aws_sdk_ec2.types.disk_info.DiskInfo"]
