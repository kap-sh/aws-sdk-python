"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMetricDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.predictive_scaling_metric_dimension

PredictiveScalingMetricDimensions: TypeAlias = list[
    "capo_application_auto_scaling.types.predictive_scaling_metric_dimension.PredictiveScalingMetricDimension"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMetricDimensions) -> list:
    import capo_application_auto_scaling.types.predictive_scaling_metric_dimension

    out: list = []
    for item in value:
        out.append(
            capo_application_auto_scaling.types.predictive_scaling_metric_dimension.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PredictiveScalingMetricDimensions:
    import capo_application_auto_scaling.types.predictive_scaling_metric_dimension

    out: PredictiveScalingMetricDimensions = []
    for item in data:
        out.append(
            capo_application_auto_scaling.types.predictive_scaling_metric_dimension.deserialize_aws_json_1_1(
                item
            )
        )
    return out
