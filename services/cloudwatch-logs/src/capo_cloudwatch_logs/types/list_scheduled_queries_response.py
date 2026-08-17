"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListScheduledQueriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.scheduled_query_summary_list


class ListScheduledQueriesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    scheduled_queries: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_summary_list.ScheduledQuerySummaryList"
    ]
    """<p>An array of scheduled query summary information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListScheduledQueriesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "scheduled_queries" in value:
        import capo_cloudwatch_logs.types.scheduled_query_summary_list

        out["scheduledQueries"] = (
            capo_cloudwatch_logs.types.scheduled_query_summary_list.serialize_aws_json_1_1(
                value["scheduled_queries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListScheduledQueriesResponse:
    out: ListScheduledQueriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("scheduledQueries") is not None:
        import capo_cloudwatch_logs.types.scheduled_query_summary_list

        out["scheduled_queries"] = (
            capo_cloudwatch_logs.types.scheduled_query_summary_list.deserialize_aws_json_1_1(
                data["scheduledQueries"]
            )
        )
    return out
