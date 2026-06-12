"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_data_query

PredictiveScalingMetricDataQueries: TypeAlias = list[
    "aws_sdk_application_auto_scaling.types.predictive_scaling_metric_data_query.PredictiveScalingMetricDataQuery"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMetricDataQueries) -> list:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_data_query

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_auto_scaling.types.predictive_scaling_metric_data_query.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PredictiveScalingMetricDataQueries:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_data_query

    out: PredictiveScalingMetricDataQueries = []
    for item in data:
        out.append(
            aws_sdk_application_auto_scaling.types.predictive_scaling_metric_data_query.deserialize_aws_json_1_1(
                item
            )
        )
    return out
