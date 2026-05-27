"""Generated from Smithy shape ``com.amazonaws.ec2#CreateStoreImageTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CreateStoreImageTaskResult(TypedDict):
    object_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the stored AMI object in the S3 bucket.</p>"""
