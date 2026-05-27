"""Generated from Smithy shape ``com.amazonaws.ec2#StorageLocation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class StorageLocation(TypedDict):
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the S3 bucket.</p>"""
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key.</p>"""
