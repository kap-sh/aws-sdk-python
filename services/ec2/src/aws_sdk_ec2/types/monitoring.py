"""Generated from Smithy shape ``com.amazonaws.ec2#Monitoring``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.monitoring_state


class Monitoring(TypedDict):
    state: NotRequired["aws_sdk_ec2.types.monitoring_state.MonitoringState"]
    """<p>Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.</p>"""
