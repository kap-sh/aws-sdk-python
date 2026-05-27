"""Generated from Smithy shape ``com.amazonaws.ecs#DeviceCgroupPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.device_cgroup_permission

DeviceCgroupPermissions: TypeAlias = list[
    "aws_sdk_ecs.types.device_cgroup_permission.DeviceCgroupPermission"
]
