"""Generated from Smithy shape ``com.amazonaws.ecs#DeviceCgroupPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.device_cgroup_permission

DeviceCgroupPermissions: TypeAlias = list[
    "aws_sdk_ecs.types.device_cgroup_permission.DeviceCgroupPermission"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceCgroupPermissions) -> list:
    import aws_sdk_ecs.types.device_cgroup_permission

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.device_cgroup_permission.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceCgroupPermissions:
    import aws_sdk_ecs.types.device_cgroup_permission

    out: DeviceCgroupPermissions = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.device_cgroup_permission.deserialize_aws_json_1_1(item)
        )
    return out
