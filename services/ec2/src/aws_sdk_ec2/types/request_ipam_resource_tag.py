"""Generated from Smithy shape ``com.amazonaws.ec2#RequestIpamResourceTag``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class RequestIpamResourceTag(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value for the tag.</p>"""
