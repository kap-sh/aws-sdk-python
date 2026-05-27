"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_status_details

VolumeStatusDetailsList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_status_details.VolumeStatusDetails"
]
