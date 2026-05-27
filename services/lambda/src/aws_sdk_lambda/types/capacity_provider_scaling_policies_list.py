"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderScalingPoliciesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.target_tracking_scaling_policy

CapacityProviderScalingPoliciesList: TypeAlias = list[
    "aws_sdk_lambda.types.target_tracking_scaling_policy.TargetTrackingScalingPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderScalingPoliciesList) -> list:
    import aws_sdk_lambda.types.target_tracking_scaling_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lambda.types.target_tracking_scaling_policy.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CapacityProviderScalingPoliciesList:
    import aws_sdk_lambda.types.target_tracking_scaling_policy

    out: CapacityProviderScalingPoliciesList = []
    for item in data:
        out.append(
            aws_sdk_lambda.types.target_tracking_scaling_policy.deserialize_json(item)
        )
    return out
