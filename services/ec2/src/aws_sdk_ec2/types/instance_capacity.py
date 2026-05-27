"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCapacity``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class InstanceCapacity(TypedDict):
    available_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances that can be launched onto the Dedicated Host based on the host's available capacity.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type supported by the Dedicated Host.</p>"""
    total_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of instances that can be launched onto the Dedicated Host if there are no instances running on it.</p>"""
