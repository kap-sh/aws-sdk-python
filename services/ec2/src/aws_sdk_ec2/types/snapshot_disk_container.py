"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotDiskContainer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.sensitive_url
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_bucket


class SnapshotDiskContainer(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the disk image being imported.</p>"""
    format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The format of the disk image being imported.</p> <p>Valid values: <code>VHD</code> | <code>VMDK</code> | <code>RAW</code> </p>"""
    url: NotRequired["aws_sdk_ec2.types.sensitive_url.SensitiveUrl"]
    """<p>The URL to the Amazon S3-based disk image being imported. It can either be a https URL (https://..) or an Amazon S3 URL (s3://..).</p>"""
    user_bucket: NotRequired["aws_sdk_ec2.types.user_bucket.UserBucket"]
    """<p>The Amazon S3 bucket for the disk image.</p>"""
