"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusEventsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_status_event

VolumeStatusEventsList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_status_event.VolumeStatusEvent"
]
