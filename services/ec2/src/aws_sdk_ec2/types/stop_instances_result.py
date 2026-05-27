"""Generated from Smithy shape ``com.amazonaws.ec2#StopInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_state_change_list


class StopInstancesResult(TypedDict):
    stopping_instances: NotRequired[
        "aws_sdk_ec2.types.instance_state_change_list.InstanceStateChangeList"
    ]
    """<p>Information about the stopped instances.</p>"""
