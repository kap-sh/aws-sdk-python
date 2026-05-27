"""Generated from Smithy shape ``com.amazonaws.ecs#MountPoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.string


class MountPoint(TypedDict):
    source_volume: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the volume to mount. Must be a volume name referenced in the <code>name</code> parameter of task definition <code>volume</code>.</p>"""
    container_path: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The path on the container to mount the host volume at.</p>"""
    read_only: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If this value is <code>true</code>, the container has read-only access to the volume. If this value is <code>false</code>, then the container can write to the volume. The default value is <code>false</code>.</p>"""
