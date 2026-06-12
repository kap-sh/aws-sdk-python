"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AggregateLogGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.aggregate_log_group_summary

AggregateLogGroupSummaries: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.aggregate_log_group_summary.AggregateLogGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateLogGroupSummaries) -> list:
    import aws_sdk_cloudwatch_logs.types.aggregate_log_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.aggregate_log_group_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregateLogGroupSummaries:
    import aws_sdk_cloudwatch_logs.types.aggregate_log_group_summary

    out: AggregateLogGroupSummaries = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.aggregate_log_group_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
