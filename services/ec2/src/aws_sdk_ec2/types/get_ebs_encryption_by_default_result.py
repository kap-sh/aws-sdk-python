"""Generated from Smithy shape ``com.amazonaws.ec2#GetEbsEncryptionByDefaultResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.sse_type


class GetEbsEncryptionByDefaultResult(TypedDict):
    ebs_encryption_by_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether encryption by default is enabled.</p>"""
    sse_type: NotRequired["aws_sdk_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""
