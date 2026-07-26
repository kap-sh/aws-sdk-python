"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderScalingPoliciesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.target_tracking_scaling_policy

CapacityProviderScalingPoliciesList: TypeAlias = list[
    "capo_lambda.types.target_tracking_scaling_policy.TargetTrackingScalingPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderScalingPoliciesList) -> list:
    import capo_lambda.types.target_tracking_scaling_policy

    out: list = []
    for item in value:
        out.append(
            capo_lambda.types.target_tracking_scaling_policy.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CapacityProviderScalingPoliciesList:
    import capo_lambda.types.target_tracking_scaling_policy

    out: CapacityProviderScalingPoliciesList = []
    for item in data:
        out.append(
            capo_lambda.types.target_tracking_scaling_policy.deserialize_json(item)
        )
    return out
