"""Generated from Smithy shape ``com.amazonaws.ec2#UnmonitorInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_monitoring_list


class UnmonitorInstancesResult(TypedDict):
    instance_monitorings: NotRequired[
        "aws_sdk_ec2.types.instance_monitoring_list.InstanceMonitoringList"
    ]
    """<p>The monitoring information.</p>"""
