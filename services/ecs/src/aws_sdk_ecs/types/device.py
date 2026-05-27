"""Generated from Smithy shape ``com.amazonaws.ecs#Device``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
