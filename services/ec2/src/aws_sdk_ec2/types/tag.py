"""Generated from Smithy shape ``com.amazonaws.ec2#Tag``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Tag(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key of the tag.</p> <p>Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with <code>aws:</code>.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the tag.</p> <p>Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.</p>"""
