"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedApplicationAutoScalingPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.managed_application_auto_scaling_policy

ManagedApplicationAutoScalingPolicies: TypeAlias = list[
    "capo_ecs.types.managed_application_auto_scaling_policy.ManagedApplicationAutoScalingPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedApplicationAutoScalingPolicies) -> list:
    import capo_ecs.types.managed_application_auto_scaling_policy

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.managed_application_auto_scaling_policy.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedApplicationAutoScalingPolicies:
    import capo_ecs.types.managed_application_auto_scaling_policy

    out: ManagedApplicationAutoScalingPolicies = []
    for item in data:
        out.append(
            capo_ecs.types.managed_application_auto_scaling_policy.deserialize_aws_json_1_1(
                item
            )
        )
    return out
