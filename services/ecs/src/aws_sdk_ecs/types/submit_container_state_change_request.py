"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitContainerStateChangeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.network_bindings
    import aws_sdk_ecs.types.string


class SubmitContainerStateChangeRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full ARN of the cluster that hosts the container.</p>"""
    task: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.</p>"""
    container_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    runtime_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the Docker container.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the state change request.</p>"""
    exit_code: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The exit code that's returned for the state change request.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the state change request.</p>"""
    network_bindings: NotRequired["aws_sdk_ecs.types.network_bindings.NetworkBindings"]
    """<p>The network bindings of the container.</p>"""
