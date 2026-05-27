"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentCapacityProvider``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.string


class DaemonDeploymentCapacityProvider(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    running_instance_count: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of instances running daemon tasks on this capacity provider.</p>"""
    draining_instance_count: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of instances being drained on this capacity provider during the deployment.</p>"""
