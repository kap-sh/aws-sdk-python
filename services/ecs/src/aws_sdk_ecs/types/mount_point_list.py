"""Generated from Smithy shape ``com.amazonaws.ecs#MountPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.mount_point

MountPointList: TypeAlias = list["aws_sdk_ecs.types.mount_point.MountPoint"]
