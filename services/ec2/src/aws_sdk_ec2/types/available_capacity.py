"""Generated from Smithy shape ``com.amazonaws.ec2#AvailableCapacity``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.available_instance_capacity_list
    import aws_sdk_ec2.types.integer


class AvailableCapacity(TypedDict):
    available_instance_capacity: NotRequired[
        "aws_sdk_ec2.types.available_instance_capacity_list.AvailableInstanceCapacityList"
    ]
    """<p>The number of instances that can be launched onto the Dedicated Host depending on the host's available capacity. For Dedicated Hosts that support multiple instance types, this parameter represents the number of instances for each instance size that is supported on the host.</p>"""
    available_v_cpus: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of vCPUs available for launching instances onto the Dedicated Host.</p>"""
