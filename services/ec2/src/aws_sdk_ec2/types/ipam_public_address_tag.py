"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressTag``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class IpamPublicAddressTag(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The tag's key.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The tag's value.</p>"""
