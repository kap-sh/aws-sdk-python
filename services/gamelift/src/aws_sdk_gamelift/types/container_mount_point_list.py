"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerMountPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_mount_point

ContainerMountPointList: TypeAlias = list[
    "aws_sdk_gamelift.types.container_mount_point.ContainerMountPoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerMountPointList) -> list:
    import aws_sdk_gamelift.types.container_mount_point

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.container_mount_point.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerMountPointList:
    import aws_sdk_gamelift.types.container_mount_point

    out: ContainerMountPointList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.container_mount_point.deserialize_aws_json_1_1(item)
        )
    return out
