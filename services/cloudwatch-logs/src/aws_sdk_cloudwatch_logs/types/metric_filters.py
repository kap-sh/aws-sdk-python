"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.metric_filter

MetricFilters: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.metric_filter.MetricFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricFilters) -> list:
    import aws_sdk_cloudwatch_logs.types.metric_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.metric_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricFilters:
    import aws_sdk_cloudwatch_logs.types.metric_filter

    out: MetricFilters = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.metric_filter.deserialize_aws_json_1_1(item)
        )
    return out
