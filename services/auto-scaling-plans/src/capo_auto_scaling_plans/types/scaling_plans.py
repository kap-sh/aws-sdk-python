"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPlans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.scaling_plan

ScalingPlans: TypeAlias = list["capo_auto_scaling_plans.types.scaling_plan.ScalingPlan"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPlans) -> list:
    import capo_auto_scaling_plans.types.scaling_plan

    out: list = []
    for item in value:
        out.append(
            capo_auto_scaling_plans.types.scaling_plan.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingPlans:
    import capo_auto_scaling_plans.types.scaling_plan

    out: ScalingPlans = []
    for item in data:
        out.append(
            capo_auto_scaling_plans.types.scaling_plan.deserialize_aws_json_1_1(item)
        )
    return out
