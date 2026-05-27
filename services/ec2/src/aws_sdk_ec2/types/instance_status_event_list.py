"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_event

InstanceStatusEventList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_status_event.InstanceStatusEvent"
]
