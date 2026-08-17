"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_summary

LogGroupSummaries: TypeAlias = list[
    "capo_cloudwatch_logs.types.log_group_summary.LogGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupSummaries) -> list:
    import capo_cloudwatch_logs.types.log_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.log_group_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogGroupSummaries:
    import capo_cloudwatch_logs.types.log_group_summary

    out: LogGroupSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.log_group_summary.deserialize_aws_json_1_1(item)
        )
    return out
