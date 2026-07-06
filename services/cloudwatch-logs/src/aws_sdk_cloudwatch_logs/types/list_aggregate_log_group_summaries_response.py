"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListAggregateLogGroupSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.aggregate_log_group_summaries
    import aws_sdk_cloudwatch_logs.types.next_token


class ListAggregateLogGroupSummariesResponse(TypedDict, closed=True):
    aggregate_log_group_summaries: NotRequired[
        "aws_sdk_cloudwatch_logs.types.aggregate_log_group_summaries.AggregateLogGroupSummaries"
    ]
    """<p>The list of aggregate log group summaries grouped by the specified data source characteristics.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAggregateLogGroupSummariesResponse) -> dict:
    out: dict = {}
    if "aggregate_log_group_summaries" in value:
        import aws_sdk_cloudwatch_logs.types.aggregate_log_group_summaries

        out["aggregateLogGroupSummaries"] = (
            aws_sdk_cloudwatch_logs.types.aggregate_log_group_summaries.serialize_aws_json_1_1(
                value["aggregate_log_group_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAggregateLogGroupSummariesResponse:
    out: ListAggregateLogGroupSummariesResponse = {}  # type: ignore[typeddict-item]
    if "aggregateLogGroupSummaries" in data:
        import aws_sdk_cloudwatch_logs.types.aggregate_log_group_summaries

        out["aggregate_log_group_summaries"] = (
            aws_sdk_cloudwatch_logs.types.aggregate_log_group_summaries.deserialize_aws_json_1_1(
                data["aggregateLogGroupSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
