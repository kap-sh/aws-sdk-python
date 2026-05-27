"""Generated from Smithy shape ``com.amazonaws.ec2#UserBucket``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class UserBucket(TypedDict):
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket where the disk image is located.</p>"""
    s3_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The file name of the disk image.</p>"""
