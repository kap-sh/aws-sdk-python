"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerTagDimension``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CapacityManagerTagDimension(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The tag key. </p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The tag value. </p>"""
