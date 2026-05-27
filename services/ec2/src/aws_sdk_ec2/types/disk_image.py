"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_image_detail
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_detail


class DiskImage(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the disk image.</p>"""
    image: NotRequired["aws_sdk_ec2.types.disk_image_detail.DiskImageDetail"]
    """<p>Information about the disk image.</p>"""
    volume: NotRequired["aws_sdk_ec2.types.volume_detail.VolumeDetail"]
    """<p>Information about the volume.</p>"""
