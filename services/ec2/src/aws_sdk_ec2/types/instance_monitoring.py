"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMonitoring``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.monitoring
    import aws_sdk_ec2.types.string


class InstanceMonitoring(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    monitoring: NotRequired["aws_sdk_ec2.types.monitoring.Monitoring"]
    """<p>The monitoring for the instance.</p>"""
