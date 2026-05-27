"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedApplicationAutoScalingPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.double
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedApplicationAutoScalingPolicy(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Application Auto Scaling policy associated with the Express service.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of Application Auto Scaling policy creation.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the Application Auto Scaling policy is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the Application Auto Scaling policy was last updated.</p>"""
    policy_type: "aws_sdk_ecs.types.string.String"
    """<p>The type of Application Auto Scaling policy associated with the Express service. Valid values are <code>TargetTrackingScaling</code>, <code>StepScaling</code>, and <code>PredictiveScaling</code>.</p>"""
    target_value: "aws_sdk_ecs.types.double.Double"
    """<p>The target value for the auto scaling metric.</p>"""
    metric: "aws_sdk_ecs.types.string.String"
    """<p>The metric used for auto scaling decisions. The available metrics are <code>ECSServiceAverageCPUUtilization</code>, <code>ECSServiceAverageMemoryUtilization</code>, and <code>ALBRequestCOuntPerTarget</code>.</p>"""
