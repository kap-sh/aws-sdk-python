"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetQueryResultsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.query_max_results
    import capo_internetmonitor.types.resource_name


class GetQueryResultsInput(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor to return data for.</p>"""
    query_id: "str"
    """<p>The ID of the query that you want to return data results for. A <code>QueryId</code> is an internally-generated identifier for a specific query.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired[
        "capo_internetmonitor.types.query_max_results.QueryMaxResults"
    ]
    """<p>The number of query results that you want to return with this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueryResultsInput:
    out: GetQueryResultsInput = {}  # type: ignore[typeddict-item]
    return out
