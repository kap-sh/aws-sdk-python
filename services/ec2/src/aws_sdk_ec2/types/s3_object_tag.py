"""Generated from Smithy shape ``com.amazonaws.ec2#S3ObjectTag``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class S3ObjectTag(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key of the tag.</p> <p>Constraints: Tag keys are case-sensitive and can be up to 128 Unicode characters in length. May not begin with <code>aws</code>:.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the tag.</p> <p>Constraints: Tag values are case-sensitive and can be up to 256 Unicode characters in length.</p>"""
