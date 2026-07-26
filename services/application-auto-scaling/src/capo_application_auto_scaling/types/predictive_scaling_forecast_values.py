"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingForecastValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.metric_scale

PredictiveScalingForecastValues: TypeAlias = list[
    "capo_application_auto_scaling.types.metric_scale.MetricScale"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingForecastValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PredictiveScalingForecastValues:
    return list(data)
