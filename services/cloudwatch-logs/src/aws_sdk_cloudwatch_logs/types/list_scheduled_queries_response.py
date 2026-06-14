"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListScheduledQueriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.scheduled_query_summary_list


class ListScheduledQueriesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    scheduled_queries: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_summary_list.ScheduledQuerySummaryList"
    ]
    """<p>An array of scheduled query summary information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListScheduledQueriesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "scheduled_queries" in value:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_summary_list

        out["scheduledQueries"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_summary_list.serialize_aws_json_1_1(
                value["scheduled_queries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListScheduledQueriesResponse:
    out: ListScheduledQueriesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "scheduledQueries" in data:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_summary_list

        out["scheduled_queries"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_summary_list.deserialize_aws_json_1_1(
                data["scheduledQueries"]
            )
        )
    return out
