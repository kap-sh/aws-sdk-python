"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_id

VolumeIdStringList: TypeAlias = list["aws_sdk_ec2.types.volume_id.VolumeId"]
