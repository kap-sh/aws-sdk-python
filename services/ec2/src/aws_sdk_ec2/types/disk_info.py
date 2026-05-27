"""Generated from Smithy shape ``com.amazonaws.ec2#DiskInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_count
    import aws_sdk_ec2.types.disk_size
    import aws_sdk_ec2.types.disk_type


class DiskInfo(TypedDict):
    size_in_gb: NotRequired["aws_sdk_ec2.types.disk_size.DiskSize"]
    """<p>The size of the disk in GB.</p>"""
    count: NotRequired["aws_sdk_ec2.types.disk_count.DiskCount"]
    """<p>The number of disks with this configuration.</p>"""
    type: NotRequired["aws_sdk_ec2.types.disk_type.DiskType"]
    """<p>The type of disk.</p>"""
