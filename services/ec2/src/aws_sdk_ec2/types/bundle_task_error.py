"""Generated from Smithy shape ``com.amazonaws.ec2#BundleTaskError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class BundleTaskError(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error message.</p>"""
