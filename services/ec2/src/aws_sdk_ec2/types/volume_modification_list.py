"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeModificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_modification

VolumeModificationList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_modification.VolumeModification"
]
