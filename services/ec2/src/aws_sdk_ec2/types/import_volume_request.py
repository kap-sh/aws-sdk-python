"""Generated from Smithy shape ``com.amazonaws.ec2#ImportVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.disk_image_detail
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_detail


class ImportVolumeRequest(TypedDict):
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone for the resulting EBS volume.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone for the resulting EBS volume.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>"""
    image: NotRequired["aws_sdk_ec2.types.disk_image_detail.DiskImageDetail"]
    """<p>The disk image.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the volume.</p>"""
    volume: NotRequired["aws_sdk_ec2.types.volume_detail.VolumeDetail"]
    """<p>The volume size.</p>"""
