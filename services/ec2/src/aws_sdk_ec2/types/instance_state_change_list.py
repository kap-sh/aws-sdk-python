"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStateChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_state_change

InstanceStateChangeList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_state_change.InstanceStateChange"
]
