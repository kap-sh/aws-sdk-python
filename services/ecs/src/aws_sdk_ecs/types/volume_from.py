"""Generated from Smithy shape ``com.amazonaws.ecs#VolumeFrom``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.string


class VolumeFrom(TypedDict):
    source_container: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of another container within the same task definition to mount volumes from.</p>"""
    read_only: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If this value is <code>true</code>, the container has read-only access to the volume. If this value is <code>false</code>, then the container can write to the volume. The default value is <code>false</code>.</p>"""
