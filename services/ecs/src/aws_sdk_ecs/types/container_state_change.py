"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerStateChange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.network_bindings
    import aws_sdk_ecs.types.string


class ContainerStateChange(TypedDict):
    container_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    image_digest: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container image SHA 256 digest.</p>"""
    runtime_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the Docker container.</p>"""
    exit_code: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The exit code for the container, if the state change is a result of the container exiting.</p>"""
    network_bindings: NotRequired["aws_sdk_ecs.types.network_bindings.NetworkBindings"]
    """<p>Any network bindings that are associated with the container.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the state change.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the container.</p>"""
