"""Generated from Smithy shape ``com.amazonaws.ecs#Device``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.device_cgroup_permissions
    import aws_sdk_ecs.types.string


class Device(TypedDict):
    host_path: "aws_sdk_ecs.types.string.String"
    """<p>The path for the device on the host container instance.</p>"""
    container_path: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The path inside the container at which to expose the host device.</p>"""
    permissions: NotRequired[
        "aws_sdk_ecs.types.device_cgroup_permissions.DeviceCgroupPermissions"
    ]
    """<p>The explicit permissions to provide to the container for the device. By default, the container has permissions for <code>read</code>, <code>write</code>, and <code>mknod</code> for the device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Device) -> dict:
    out: dict = {}
    out["hostPath"] = value["host_path"]
    if "container_path" in value:
        out["containerPath"] = value["container_path"]
    if "permissions" in value:
        import aws_sdk_ecs.types.device_cgroup_permissions

        out["permissions"] = (
            aws_sdk_ecs.types.device_cgroup_permissions.serialize_aws_json_1_1(
                value["permissions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if "hostPath" in data:
        out["host_path"] = data["hostPath"]
    else:
        raise DeserializationError("Device.host_path required")
    if "containerPath" in data:
        out["container_path"] = data["containerPath"]
    if "permissions" in data:
        import aws_sdk_ecs.types.device_cgroup_permissions

        out["permissions"] = (
            aws_sdk_ecs.types.device_cgroup_permissions.deserialize_aws_json_1_1(
                data["permissions"]
            )
        )
    return out
