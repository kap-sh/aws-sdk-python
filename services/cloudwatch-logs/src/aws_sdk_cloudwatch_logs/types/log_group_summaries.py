"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_summary

LogGroupSummaries: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.log_group_summary.LogGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupSummaries) -> list:
    import aws_sdk_cloudwatch_logs.types.log_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.log_group_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogGroupSummaries:
    import aws_sdk_cloudwatch_logs.types.log_group_summary

    out: LogGroupSummaries = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.log_group_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
