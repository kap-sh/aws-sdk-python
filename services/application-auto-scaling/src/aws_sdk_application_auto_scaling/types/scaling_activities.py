"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalingActivities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.scaling_activity

ScalingActivities: TypeAlias = list[
    "aws_sdk_application_auto_scaling.types.scaling_activity.ScalingActivity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingActivities) -> list:
    import aws_sdk_application_auto_scaling.types.scaling_activity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_auto_scaling.types.scaling_activity.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingActivities:
    import aws_sdk_application_auto_scaling.types.scaling_activity

    out: ScalingActivities = []
    for item in data:
        out.append(
            aws_sdk_application_auto_scaling.types.scaling_activity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
