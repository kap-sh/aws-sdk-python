"""Generated from Smithy shape ``com.amazonaws.ecs#VolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.volume

VolumeList: TypeAlias = list["aws_sdk_ecs.types.volume.Volume"]
