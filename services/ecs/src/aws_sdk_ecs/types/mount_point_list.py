"""Generated from Smithy shape ``com.amazonaws.ecs#MountPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.mount_point

MountPointList: TypeAlias = list["aws_sdk_ecs.types.mount_point.MountPoint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MountPointList) -> list:
    import aws_sdk_ecs.types.mount_point

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.mount_point.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MountPointList:
    import aws_sdk_ecs.types.mount_point

    out: MountPointList = []
    for item in data:
        out.append(aws_sdk_ecs.types.mount_point.deserialize_aws_json_1_1(item))
    return out
