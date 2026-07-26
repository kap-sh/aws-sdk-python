"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalingActivities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.scaling_activity

ScalingActivities: TypeAlias = list[
    "capo_application_auto_scaling.types.scaling_activity.ScalingActivity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingActivities) -> list:
    import capo_application_auto_scaling.types.scaling_activity

    out: list = []
    for item in value:
        out.append(
            capo_application_auto_scaling.types.scaling_activity.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingActivities:
    import capo_application_auto_scaling.types.scaling_activity

    out: ScalingActivities = []
    for item in data:
        out.append(
            capo_application_auto_scaling.types.scaling_activity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
