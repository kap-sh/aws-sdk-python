"""Generated from Smithy shape ``com.amazonaws.ec2#IpamCidrAuthorizationContext``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class IpamCidrAuthorizationContext(TypedDict):
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The plain-text authorization message for the prefix and account.</p>"""
    signature: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The signed authorization message for the prefix and account.</p>"""
