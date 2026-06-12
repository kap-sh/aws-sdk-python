"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#TargetTrackingMetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.target_tracking_metric_data_query

TargetTrackingMetricDataQueries: TypeAlias = list[
    "aws_sdk_application_auto_scaling.types.target_tracking_metric_data_query.TargetTrackingMetricDataQuery"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingMetricDataQueries) -> list:
    import aws_sdk_application_auto_scaling.types.target_tracking_metric_data_query

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_auto_scaling.types.target_tracking_metric_data_query.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetTrackingMetricDataQueries:
    import aws_sdk_application_auto_scaling.types.target_tracking_metric_data_query

    out: TargetTrackingMetricDataQueries = []
    for item in data:
        out.append(
            aws_sdk_application_auto_scaling.types.target_tracking_metric_data_query.deserialize_aws_json_1_1(
                item
            )
        )
    return out
