"""Generated from Smithy shape ``com.amazonaws.batch#DeviceCgroupPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.device_cgroup_permission

DeviceCgroupPermissions: TypeAlias = list[
    "aws_sdk_batch.types.device_cgroup_permission.DeviceCgroupPermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceCgroupPermissions) -> list:
    import aws_sdk_batch.types.device_cgroup_permission

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.device_cgroup_permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceCgroupPermissions:
    import aws_sdk_batch.types.device_cgroup_permission

    out: DeviceCgroupPermissions = []
    for item in data:
        out.append(aws_sdk_batch.types.device_cgroup_permission.deserialize_json(item))
    return out
