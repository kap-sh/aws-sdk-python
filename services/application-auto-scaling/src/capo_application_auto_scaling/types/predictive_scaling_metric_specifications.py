"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMetricSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.predictive_scaling_metric_specification

PredictiveScalingMetricSpecifications: TypeAlias = list[
    "capo_application_auto_scaling.types.predictive_scaling_metric_specification.PredictiveScalingMetricSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMetricSpecifications) -> list:
    import capo_application_auto_scaling.types.predictive_scaling_metric_specification

    out: list = []
    for item in value:
        out.append(
            capo_application_auto_scaling.types.predictive_scaling_metric_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PredictiveScalingMetricSpecifications:
    import capo_application_auto_scaling.types.predictive_scaling_metric_specification

    out: PredictiveScalingMetricSpecifications = []
    for item in data:
        out.append(
            capo_application_auto_scaling.types.predictive_scaling_metric_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
