"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#TargetTrackingConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.target_tracking_configuration

TargetTrackingConfigurations: TypeAlias = list[
    "aws_sdk_auto_scaling_plans.types.target_tracking_configuration.TargetTrackingConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingConfigurations) -> list:
    import aws_sdk_auto_scaling_plans.types.target_tracking_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auto_scaling_plans.types.target_tracking_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetTrackingConfigurations:
    import aws_sdk_auto_scaling_plans.types.target_tracking_configuration

    out: TargetTrackingConfigurations = []
    for item in data:
        out.append(
            aws_sdk_auto_scaling_plans.types.target_tracking_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
