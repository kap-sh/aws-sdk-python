"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ListScheduledQueriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.max_scheduled_queries_results
    import capo_timestream_query.types.next_scheduled_queries_results_token


class ListScheduledQueriesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_timestream_query.types.max_scheduled_queries_results.MaxScheduledQueriesResults"
    ]
    """<p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a <code>NextToken</code> is provided in the output. To resume pagination, provide the <code>NextToken</code> value as the argument to the subsequent call to <code>ListScheduledQueriesRequest</code>.</p>"""
    next_token: NotRequired[
        "capo_timestream_query.types.next_scheduled_queries_results_token.NextScheduledQueriesResultsToken"
    ]
    """<p> A pagination token to resume pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListScheduledQueriesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListScheduledQueriesRequest:
    out: ListScheduledQueriesRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
