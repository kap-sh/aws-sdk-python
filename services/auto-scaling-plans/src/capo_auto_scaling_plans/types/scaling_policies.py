"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.scaling_policy

ScalingPolicies: TypeAlias = list[
    "capo_auto_scaling_plans.types.scaling_policy.ScalingPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicies) -> list:
    import capo_auto_scaling_plans.types.scaling_policy

    out: list = []
    for item in value:
        out.append(
            capo_auto_scaling_plans.types.scaling_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingPolicies:
    import capo_auto_scaling_plans.types.scaling_policy

    out: ScalingPolicies = []
    for item in data:
        out.append(
            capo_auto_scaling_plans.types.scaling_policy.deserialize_aws_json_1_1(item)
        )
    return out
