"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPlanNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.scaling_plan_name

ScalingPlanNames: TypeAlias = list[
    "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPlanNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ScalingPlanNames:
    return list(data)
