"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStateChange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_state
    import aws_sdk_ec2.types.string


class InstanceStateChange(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    current_state: NotRequired["aws_sdk_ec2.types.instance_state.InstanceState"]
    """<p>The current state of the instance.</p>"""
    previous_state: NotRequired["aws_sdk_ec2.types.instance_state.InstanceState"]
    """<p>The previous state of the instance.</p>"""
