"""Generated from Smithy shape ``com.amazonaws.ec2#Storage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.s3_storage


class Storage(TypedDict):
    s3: NotRequired["aws_sdk_ec2.types.s3_storage.S3Storage"]
    """<p>An Amazon S3 storage location.</p>"""
