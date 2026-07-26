"""Generated from Smithy shape ``com.amazonaws.batch#Device``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.device_cgroup_permissions
    import capo_batch.types.string


class Device(TypedDict, closed=True):
    host_path: NotRequired["capo_batch.types.string.String"]
    """<p>The path for the device on the host container instance.</p>"""
    container_path: NotRequired["capo_batch.types.string.String"]
    """<p>The path inside the container that's used to expose the host device. By default, the <code>hostPath</code> value is used.</p>"""
    permissions: NotRequired[
        "capo_batch.types.device_cgroup_permissions.DeviceCgroupPermissions"
    ]
    """<p>The explicit permissions to provide to the container for the device. By default, the container has permissions for <code>read</code>, <code>write</code>, and <code>mknod</code> for the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Device) -> dict:
    out: dict = {}
    if "host_path" in value:
        out["hostPath"] = value["host_path"]
    if "container_path" in value:
        out["containerPath"] = value["container_path"]
    if "permissions" in value:
        import capo_batch.types.device_cgroup_permissions

        out["permissions"] = capo_batch.types.device_cgroup_permissions.serialize_json(
            value["permissions"]
        )
    return out


def deserialize_json(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if "hostPath" in data:
        out["host_path"] = data["hostPath"]
    if "containerPath" in data:
        out["container_path"] = data["containerPath"]
    if "permissions" in data:
        import capo_batch.types.device_cgroup_permissions

        out["permissions"] = (
            capo_batch.types.device_cgroup_permissions.deserialize_json(
                data["permissions"]
            )
        )
    return out
