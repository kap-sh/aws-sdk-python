"""Generated from Smithy shape ``com.amazonaws.ec2#MonitorInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_monitoring_list


class MonitorInstancesResult(TypedDict):
    instance_monitorings: NotRequired[
        "aws_sdk_ec2.types.instance_monitoring_list.InstanceMonitoringList"
    ]
    """<p>The monitoring information.</p>"""
