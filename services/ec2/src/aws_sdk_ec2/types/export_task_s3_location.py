"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTaskS3Location``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ExportTaskS3Location(TypedDict):
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination Amazon S3 bucket.</p>"""
    s3_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix (logical hierarchy) in the bucket.</p>"""
