"""Generated from Smithy shape ``com.amazonaws.ec2#BlobAttributeValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.blob


class BlobAttributeValue(TypedDict):
    value: NotRequired["aws_sdk_ec2.types.blob.Blob"]
