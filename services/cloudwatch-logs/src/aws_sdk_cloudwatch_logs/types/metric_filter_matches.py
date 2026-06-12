"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricFilterMatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.metric_filter_match_record

MetricFilterMatches: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.metric_filter_match_record.MetricFilterMatchRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricFilterMatches) -> list:
    import aws_sdk_cloudwatch_logs.types.metric_filter_match_record

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.metric_filter_match_record.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricFilterMatches:
    import aws_sdk_cloudwatch_logs.types.metric_filter_match_record

    out: MetricFilterMatches = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.metric_filter_match_record.deserialize_aws_json_1_1(
                item
            )
        )
    return out
