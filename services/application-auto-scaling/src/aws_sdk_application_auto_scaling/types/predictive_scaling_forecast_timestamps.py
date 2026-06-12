"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingForecastTimestamps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.timestamp_type

PredictiveScalingForecastTimestamps: TypeAlias = list[
    "aws_sdk_application_auto_scaling.types.timestamp_type.TimestampType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingForecastTimestamps) -> list:
    import aws_sdk_application_auto_scaling.types.timestamp_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_auto_scaling.types.timestamp_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PredictiveScalingForecastTimestamps:
    import aws_sdk_application_auto_scaling.types.timestamp_type

    out: PredictiveScalingForecastTimestamps = []
    for item in data:
        out.append(
            aws_sdk_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
