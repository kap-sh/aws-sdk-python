"""Generated from Smithy shape ``com.amazonaws.ec2#UserBucketDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class UserBucketDetails(TypedDict):
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon S3 bucket from which the disk image was created.</p>"""
    s3_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The file name of the disk image.</p>"""
