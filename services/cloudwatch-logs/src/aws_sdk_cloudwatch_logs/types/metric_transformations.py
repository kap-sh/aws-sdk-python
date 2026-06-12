"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricTransformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.metric_transformation

MetricTransformations: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.metric_transformation.MetricTransformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricTransformations) -> list:
    import aws_sdk_cloudwatch_logs.types.metric_transformation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.metric_transformation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricTransformations:
    import aws_sdk_cloudwatch_logs.types.metric_transformation

    out: MetricTransformations = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.metric_transformation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
