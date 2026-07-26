"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryResultsWorkloadInsightsTopContributorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.scope_id


class GetQueryResultsWorkloadInsightsTopContributorsInput(TypedDict, closed=True):
    scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>"""
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired["int"]
    """<p>The number of query results that you want to return with this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsWorkloadInsightsTopContributorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueryResultsWorkloadInsightsTopContributorsInput:
    out: GetQueryResultsWorkloadInsightsTopContributorsInput = {}  # type: ignore[typeddict-item]
    return out
