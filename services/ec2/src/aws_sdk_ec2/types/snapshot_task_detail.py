"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotTaskDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.sensitive_url
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_bucket_details


class SnapshotTaskDetail(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the disk image being imported.</p>"""
    disk_image_size: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The size of the disk in the snapshot, in GiB.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is encrypted.</p>"""
    format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The format of the disk image from which the snapshot is created.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The identifier for the KMS key that was used to create the encrypted snapshot.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The percentage of completion for the import snapshot task.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The snapshot ID of the disk being imported.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief status for the import snapshot task.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A detailed status message for the import snapshot task.</p>"""
    url: NotRequired["aws_sdk_ec2.types.sensitive_url.SensitiveUrl"]
    """<p>The URL of the disk image from which the snapshot is created.</p>"""
    user_bucket: NotRequired["aws_sdk_ec2.types.user_bucket_details.UserBucketDetails"]
    """<p>The Amazon S3 bucket for the disk image.</p>"""
