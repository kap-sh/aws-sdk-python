"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceHealthStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.instance_health_check_result_list
    import aws_sdk_ecs.types.instance_health_check_state


class ContainerInstanceHealthStatus(TypedDict):
    overall_status: NotRequired[
        "aws_sdk_ecs.types.instance_health_check_state.InstanceHealthCheckState"
    ]
    """<p>The overall health status of the container instance. This is an aggregate status of all container instance health checks.</p>"""
    details: NotRequired[
        "aws_sdk_ecs.types.instance_health_check_result_list.InstanceHealthCheckResultList"
    ]
    """<p>An array of objects representing the details of the container instance health status.</p>"""
