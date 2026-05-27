"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.double
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string


class ServiceRevisionSummary(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service revision.</p>"""
    requested_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of requested tasks for the service revision.</p>"""
    running_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of running tasks for the service revision.</p>"""
    pending_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of pending tasks for the service revision.</p>"""
    requested_test_traffic_weight: "aws_sdk_ecs.types.double.Double"
    """<p>The percentage of test traffic that is directed to this service revision. This value represents a snapshot of the traffic distribution and may not reflect real-time changes during active deployments. Valid values are 0.0 to 100.0.</p>"""
    requested_production_traffic_weight: "aws_sdk_ecs.types.double.Double"
    """<p>The percentage of production traffic that is directed to this service revision. This value represents a snapshot of the traffic distribution and may not reflect real-time changes during active deployments. Valid values are 0.0 to 100.0.</p>"""
