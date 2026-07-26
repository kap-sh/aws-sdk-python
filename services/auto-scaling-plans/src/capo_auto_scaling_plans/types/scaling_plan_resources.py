"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPlanResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.scaling_plan_resource

ScalingPlanResources: TypeAlias = list[
    "capo_auto_scaling_plans.types.scaling_plan_resource.ScalingPlanResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPlanResources) -> list:
    import capo_auto_scaling_plans.types.scaling_plan_resource

    out: list = []
    for item in value:
        out.append(
            capo_auto_scaling_plans.types.scaling_plan_resource.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingPlanResources:
    import capo_auto_scaling_plans.types.scaling_plan_resource

    out: ScalingPlanResources = []
    for item in data:
        out.append(
            capo_auto_scaling_plans.types.scaling_plan_resource.deserialize_aws_json_1_1(
                item
            )
        )
    return out
