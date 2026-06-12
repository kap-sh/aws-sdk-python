"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#TargetTrackingMetricDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.target_tracking_metric_dimension

TargetTrackingMetricDimensions: TypeAlias = list[
    "aws_sdk_application_auto_scaling.types.target_tracking_metric_dimension.TargetTrackingMetricDimension"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingMetricDimensions) -> list:
    import aws_sdk_application_auto_scaling.types.target_tracking_metric_dimension

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_auto_scaling.types.target_tracking_metric_dimension.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetTrackingMetricDimensions:
    import aws_sdk_application_auto_scaling.types.target_tracking_metric_dimension

    out: TargetTrackingMetricDimensions = []
    for item in data:
        out.append(
            aws_sdk_application_auto_scaling.types.target_tracking_metric_dimension.deserialize_aws_json_1_1(
                item
            )
        )
    return out
