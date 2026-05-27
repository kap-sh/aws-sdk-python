"""Generated from Smithy shape ``com.amazonaws.ec2#HibernationOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class HibernationOptions(TypedDict):
    configured: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, your instance is enabled for hibernation; otherwise, it is not enabled for hibernation.</p>"""
