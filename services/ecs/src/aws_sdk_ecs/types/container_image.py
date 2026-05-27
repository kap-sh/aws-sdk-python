"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerImage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ContainerImage(TypedDict):
    container_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    image_digest: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container image digest.</p>"""
    image: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container image. </p>"""
