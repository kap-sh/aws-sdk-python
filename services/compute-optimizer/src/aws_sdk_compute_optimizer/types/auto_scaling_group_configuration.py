"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingGroupConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.allocation_strategy
    import aws_sdk_compute_optimizer.types.asg_type
    import aws_sdk_compute_optimizer.types.desired_capacity
    import aws_sdk_compute_optimizer.types.max_size
    import aws_sdk_compute_optimizer.types.min_size
    import aws_sdk_compute_optimizer.types.mixed_instance_types
    import aws_sdk_compute_optimizer.types.nullable_estimated_instance_hour_reduction_percentage
    import aws_sdk_compute_optimizer.types.nullable_instance_type


class AutoScalingGroupConfiguration(TypedDict):
    desired_capacity: "aws_sdk_compute_optimizer.types.desired_capacity.DesiredCapacity"
    """<p>The desired capacity, or number of instances, for the EC2 Auto Scaling group.</p>"""
    min_size: "aws_sdk_compute_optimizer.types.min_size.MinSize"
    """<p>The minimum size, or minimum number of instances, for the EC2 Auto Scaling group.</p>"""
    max_size: "aws_sdk_compute_optimizer.types.max_size.MaxSize"
    """<p>The maximum size, or maximum number of instances, for the EC2 Auto Scaling group.</p>"""
    instance_type: NotRequired[
        "aws_sdk_compute_optimizer.types.nullable_instance_type.NullableInstanceType"
    ]
    """<p>The instance type for the EC2 Auto Scaling group.</p>"""
    allocation_strategy: NotRequired[
        "aws_sdk_compute_optimizer.types.allocation_strategy.AllocationStrategy"
    ]
    """<p> Describes the allocation strategy that the EC2 Auto Scaling group uses. This field is only available for EC2 Auto Scaling groups with mixed instance types. </p>"""
    estimated_instance_hour_reduction_percentage: NotRequired[
        "aws_sdk_compute_optimizer.types.nullable_estimated_instance_hour_reduction_percentage.NullableEstimatedInstanceHourReductionPercentage"
    ]
    """<p> Describes the projected percentage reduction in instance hours after adopting the recommended configuration. This field is only available for EC2 Auto Scaling groups with scaling policies. </p>"""
    type: NotRequired["aws_sdk_compute_optimizer.types.asg_type.AsgType"]
    """<p> Describes whether the EC2 Auto Scaling group has a single instance type or a mixed instance type configuration. </p>"""
    mixed_instance_types: NotRequired[
        "aws_sdk_compute_optimizer.types.mixed_instance_types.MixedInstanceTypes"
    ]
    """<p> List the instance types within an EC2 Auto Scaling group that has mixed instance types. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingGroupConfiguration) -> dict:
    out: dict = {}
    out["desiredCapacity"] = value.get("desired_capacity", 0)
    out["minSize"] = value.get("min_size", 0)
    out["maxSize"] = value.get("max_size", 0)
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "allocation_strategy" in value:
        import aws_sdk_compute_optimizer.types.allocation_strategy

        out["allocationStrategy"] = (
            aws_sdk_compute_optimizer.types.allocation_strategy.serialize_aws_json_1_0(
                value["allocation_strategy"]
            )
        )
    if "estimated_instance_hour_reduction_percentage" in value:
        out["estimatedInstanceHourReductionPercentage"] = value[
            "estimated_instance_hour_reduction_percentage"
        ]
    if "type" in value:
        import aws_sdk_compute_optimizer.types.asg_type

        out["type"] = aws_sdk_compute_optimizer.types.asg_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "mixed_instance_types" in value:
        import aws_sdk_compute_optimizer.types.mixed_instance_types

        out["mixedInstanceTypes"] = (
            aws_sdk_compute_optimizer.types.mixed_instance_types.serialize_aws_json_1_0(
                value["mixed_instance_types"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingGroupConfiguration:
    out: AutoScalingGroupConfiguration = {}  # type: ignore[typeddict-item]
    if "desiredCapacity" in data:
        out["desired_capacity"] = data["desiredCapacity"]
    else:
        out["desired_capacity"] = 0
    if "minSize" in data:
        out["min_size"] = data["minSize"]
    else:
        out["min_size"] = 0
    if "maxSize" in data:
        out["max_size"] = data["maxSize"]
    else:
        out["max_size"] = 0
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "allocationStrategy" in data:
        import aws_sdk_compute_optimizer.types.allocation_strategy

        out["allocation_strategy"] = (
            aws_sdk_compute_optimizer.types.allocation_strategy.deserialize_aws_json_1_0(
                data["allocationStrategy"]
            )
        )
    if "estimatedInstanceHourReductionPercentage" in data:
        out["estimated_instance_hour_reduction_percentage"] = data[
            "estimatedInstanceHourReductionPercentage"
        ]
    if "type" in data:
        import aws_sdk_compute_optimizer.types.asg_type

        out["type"] = aws_sdk_compute_optimizer.types.asg_type.deserialize_aws_json_1_0(
            data["type"]
        )
    if "mixedInstanceTypes" in data:
        import aws_sdk_compute_optimizer.types.mixed_instance_types

        out["mixed_instance_types"] = (
            aws_sdk_compute_optimizer.types.mixed_instance_types.deserialize_aws_json_1_0(
                data["mixedInstanceTypes"]
            )
        )
    return out
