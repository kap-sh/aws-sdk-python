"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.sensitive_url
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_bucket_details


class SnapshotDetail(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the snapshot.</p>"""
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The block device mapping for the snapshot.</p>"""
    disk_image_size: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The size of the disk in the snapshot, in GiB.</p>"""
    format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The format of the disk image from which the snapshot is created.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The percentage of progress for the task.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The snapshot ID of the disk being imported.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief status of the snapshot creation.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A detailed status message for the snapshot creation.</p>"""
    url: NotRequired["aws_sdk_ec2.types.sensitive_url.SensitiveUrl"]
    """<p>The URL used to access the disk image.</p>"""
    user_bucket: NotRequired["aws_sdk_ec2.types.user_bucket_details.UserBucketDetails"]
    """<p>The Amazon S3 bucket for the disk image.</p>"""
