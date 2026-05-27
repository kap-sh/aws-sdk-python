"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplatesMonitoringRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class LaunchTemplatesMonitoringRequest(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specify <code>true</code> to enable detailed monitoring. Otherwise, basic monitoring is enabled.</p>"""
