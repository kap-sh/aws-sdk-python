"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplatesMonitoring``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class LaunchTemplatesMonitoring(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.</p>"""
