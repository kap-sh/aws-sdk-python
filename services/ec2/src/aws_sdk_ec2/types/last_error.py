"""Generated from Smithy shape ``com.amazonaws.ec2#LastError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class LastError(TypedDict):
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error message for the VPC endpoint error.</p>"""
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error code for the VPC endpoint error.</p>"""
