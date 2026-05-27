"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateHibernationOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class LaunchTemplateHibernationOptionsRequest(TypedDict):
    configured: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If you set this parameter to <code>true</code>, the instance is enabled for hibernation.</p> <p>Default: <code>false</code> </p>"""
