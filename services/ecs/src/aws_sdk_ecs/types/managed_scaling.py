"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedScaling``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_scaling_instance_warmup_period
    import aws_sdk_ecs.types.managed_scaling_status
    import aws_sdk_ecs.types.managed_scaling_step_size
    import aws_sdk_ecs.types.managed_scaling_target_capacity


class ManagedScaling(TypedDict):
    status: NotRequired["aws_sdk_ecs.types.managed_scaling_status.ManagedScalingStatus"]
    """<p>Determines whether to use managed scaling for the capacity provider.</p>"""
    target_capacity: NotRequired[
        "aws_sdk_ecs.types.managed_scaling_target_capacity.ManagedScalingTargetCapacity"
    ]
    """<p>The target capacity utilization as a percentage for the capacity provider. The specified value must be greater than <code>0</code> and less than or equal to <code>100</code>. For example, if you want the capacity provider to maintain 10% spare capacity, then that means the utilization is 90%, so use a <code>targetCapacity</code> of <code>90</code>. The default value of <code>100</code> percent results in the Amazon EC2 instances in your Auto Scaling group being completely used.</p>"""
    minimum_scaling_step_size: NotRequired[
        "aws_sdk_ecs.types.managed_scaling_step_size.ManagedScalingStepSize"
    ]
    """<p>The minimum number of Amazon EC2 instances that Amazon ECS will scale out at one time. The scale in process is not affected by this parameter If this parameter is omitted, the default value of <code>1</code> is used.</p> <p>When additional capacity is required, Amazon ECS will scale up the minimum scaling step size even if the actual demand is less than the minimum scaling step size.</p>"""
    maximum_scaling_step_size: NotRequired[
        "aws_sdk_ecs.types.managed_scaling_step_size.ManagedScalingStepSize"
    ]
    """<p>The maximum number of Amazon EC2 instances that Amazon ECS will scale out at one time. If this parameter is omitted, the default value of <code>10000</code> is used.</p>"""
    instance_warmup_period: NotRequired[
        "aws_sdk_ecs.types.managed_scaling_instance_warmup_period.ManagedScalingInstanceWarmupPeriod"
    ]
    """<p>The period of time, in seconds, after a newly launched Amazon EC2 instance can contribute to CloudWatch metrics for Auto Scaling group. If this parameter is omitted, the default value of <code>300</code> seconds is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedScaling) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_ecs.types.managed_scaling_status

        out["status"] = aws_sdk_ecs.types.managed_scaling_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "target_capacity" in value:
        out["targetCapacity"] = value["target_capacity"]
    if "minimum_scaling_step_size" in value:
        out["minimumScalingStepSize"] = value["minimum_scaling_step_size"]
    if "maximum_scaling_step_size" in value:
        out["maximumScalingStepSize"] = value["maximum_scaling_step_size"]
    if "instance_warmup_period" in value:
        out["instanceWarmupPeriod"] = value["instance_warmup_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedScaling:
    out: ManagedScaling = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_ecs.types.managed_scaling_status

        out["status"] = (
            aws_sdk_ecs.types.managed_scaling_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "targetCapacity" in data:
        out["target_capacity"] = data["targetCapacity"]
    if "minimumScalingStepSize" in data:
        out["minimum_scaling_step_size"] = data["minimumScalingStepSize"]
    if "maximumScalingStepSize" in data:
        out["maximum_scaling_step_size"] = data["maximumScalingStepSize"]
    if "instanceWarmupPeriod" in data:
        out["instance_warmup_period"] = data["instanceWarmupPeriod"]
    return out
