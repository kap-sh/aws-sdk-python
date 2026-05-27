"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonVolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_volume

DaemonVolumeList: TypeAlias = list["aws_sdk_ecs.types.daemon_volume.DaemonVolume"]
