"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateHibernationOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class LaunchTemplateHibernationOptions(TypedDict):
    configured: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If this parameter is set to <code>true</code>, the instance is enabled for hibernation; otherwise, it is not enabled for hibernation.</p>"""
