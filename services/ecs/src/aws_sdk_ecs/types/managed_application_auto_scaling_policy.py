"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedApplicationAutoScalingPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedApplicationAutoScalingPolicy) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import aws_sdk_ecs.types.managed_resource_status

    out["status"] = aws_sdk_ecs.types.managed_resource_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import aws_sdk_ecs.types.timestamp

    out["updatedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    out["policyType"] = value["policy_type"]
    out["targetValue"] = value.get("target_value", 0)
    out["metric"] = value["metric"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedApplicationAutoScalingPolicy:
    out: ManagedApplicationAutoScalingPolicy = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import aws_sdk_ecs.types.managed_resource_status

        out["status"] = (
            aws_sdk_ecs.types.managed_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedApplicationAutoScalingPolicy.status required"
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "updatedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["updated_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "ManagedApplicationAutoScalingPolicy.updated_at required"
        )
    if "policyType" in data:
        out["policy_type"] = data["policyType"]
    else:
        raise DeserializationError(
            "ManagedApplicationAutoScalingPolicy.policy_type required"
        )
    if "targetValue" in data:
        out["target_value"] = data["targetValue"]
    else:
        out["target_value"] = 0
    if "metric" in data:
        out["metric"] = data["metric"]
    else:
        raise DeserializationError(
            "ManagedApplicationAutoScalingPolicy.metric required"
        )
    return out
