"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceVolumeDetailItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_image_description
    import aws_sdk_ec2.types.disk_image_volume_description
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string


class ImportInstanceVolumeDetailItem(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone where the resulting instance will reside.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone where the resulting instance will reside.</p>"""
    bytes_converted: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The number of bytes converted so far.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the task.</p>"""
    image: NotRequired["aws_sdk_ec2.types.disk_image_description.DiskImageDescription"]
    """<p>The image.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the import of this particular disk image.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status information or errors related to the disk image.</p>"""
    volume: NotRequired[
        "aws_sdk_ec2.types.disk_image_volume_description.DiskImageVolumeDescription"
    ]
    """<p>The volume.</p>"""
