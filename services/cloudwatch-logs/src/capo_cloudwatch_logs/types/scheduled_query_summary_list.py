"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduledQuerySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.scheduled_query_summary

ScheduledQuerySummaryList: TypeAlias = list[
    "capo_cloudwatch_logs.types.scheduled_query_summary.ScheduledQuerySummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledQuerySummaryList) -> list:
    import capo_cloudwatch_logs.types.scheduled_query_summary

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.scheduled_query_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScheduledQuerySummaryList:
    import capo_cloudwatch_logs.types.scheduled_query_summary

    out: ScheduledQuerySummaryList = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.scheduled_query_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
