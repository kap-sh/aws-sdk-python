"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.instance_health_check_state
    import aws_sdk_ecs.types.instance_health_check_type
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class InstanceHealthCheckResult(TypedDict):
    type: NotRequired[
        "aws_sdk_ecs.types.instance_health_check_type.InstanceHealthCheckType"
    ]
    """<p>The type of container instance health status that was verified.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.instance_health_check_state.InstanceHealthCheckState"
    ]
    """<p>The container instance health status.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the container instance health status.</p>"""
    last_updated: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the container instance health status was last updated.</p>"""
    last_status_change: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the container instance health status last changed.</p>"""
