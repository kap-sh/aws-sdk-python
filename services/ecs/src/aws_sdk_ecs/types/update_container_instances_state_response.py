"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateContainerInstancesStateResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instances
    import aws_sdk_ecs.types.failures


class UpdateContainerInstancesStateResponse(TypedDict):
    container_instances: NotRequired[
        "aws_sdk_ecs.types.container_instances.ContainerInstances"
    ]
    """<p>The list of container instances.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
