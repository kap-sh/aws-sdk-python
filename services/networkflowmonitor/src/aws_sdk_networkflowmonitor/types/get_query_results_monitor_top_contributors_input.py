"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryResultsMonitorTopContributorsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.resource_name


class GetQueryResultsMonitorTopContributorsInput(TypedDict):
    monitor_name: "aws_sdk_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired["int"]
    """<p>The number of query results that you want to return with this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsMonitorTopContributorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueryResultsMonitorTopContributorsInput:
    out: GetQueryResultsMonitorTopContributorsInput = {}  # type: ignore[typeddict-item]
    return out
