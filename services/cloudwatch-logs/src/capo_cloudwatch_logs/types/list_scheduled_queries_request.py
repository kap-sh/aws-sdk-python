"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListScheduledQueriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.list_scheduled_queries_max_results
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.scheduled_query_state


class ListScheduledQueriesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_cloudwatch_logs.types.list_scheduled_queries_max_results.ListScheduledQueriesMaxResults"
    ]
    """<p>The maximum number of scheduled queries to return. Valid range is 1 to 1000.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    state: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
    ]
    """<p>Filter scheduled queries by state. Valid values are <code>ENABLED</code> and <code>DISABLED</code>. If not specified, all scheduled queries are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListScheduledQueriesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "state" in value:
        import capo_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            capo_cloudwatch_logs.types.scheduled_query_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListScheduledQueriesRequest:
    out: ListScheduledQueriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("state") is not None:
        import capo_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            capo_cloudwatch_logs.types.scheduled_query_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    return out
