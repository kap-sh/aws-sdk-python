"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerMountPoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_mount_point_access_level
    import aws_sdk_gamelift.types.container_path_string
    import aws_sdk_gamelift.types.instance_path_string


class ContainerMountPoint(TypedDict):
    instance_path: NotRequired[
        "aws_sdk_gamelift.types.instance_path_string.InstancePathString"
    ]
    """<p>The path to the source file or directory. </p>"""
    container_path: NotRequired[
        "aws_sdk_gamelift.types.container_path_string.ContainerPathString"
    ]
    """<p>The mount path on the container. If this property isn't set, the instance path is used.</p>"""
    access_level: NotRequired[
        "aws_sdk_gamelift.types.container_mount_point_access_level.ContainerMountPointAccessLevel"
    ]
    """<p>The type of access for the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerMountPoint) -> dict:
    out: dict = {}
    if "instance_path" in value:
        out["InstancePath"] = value["instance_path"]
    if "container_path" in value:
        out["ContainerPath"] = value["container_path"]
    if "access_level" in value:
        import aws_sdk_gamelift.types.container_mount_point_access_level

        out["AccessLevel"] = (
            aws_sdk_gamelift.types.container_mount_point_access_level.serialize_aws_json_1_1(
                value["access_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerMountPoint:
    out: ContainerMountPoint = {}  # type: ignore[typeddict-item]
    if "InstancePath" in data:
        out["instance_path"] = data["InstancePath"]
    if "ContainerPath" in data:
        out["container_path"] = data["ContainerPath"]
    if "AccessLevel" in data:
        import aws_sdk_gamelift.types.container_mount_point_access_level

        out["access_level"] = (
            aws_sdk_gamelift.types.container_mount_point_access_level.deserialize_aws_json_1_1(
                data["AccessLevel"]
            )
        )
    return out
