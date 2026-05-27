"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume

VolumeList: TypeAlias = list["aws_sdk_ec2.types.volume.Volume"]
