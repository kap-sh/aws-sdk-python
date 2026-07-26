"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.environment_state_list
    import capo_evs.types.max_results
    import capo_evs.types.pagination_token


class ListEnvironmentsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""
    max_results: NotRequired["capo_evs.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>"""
    state: NotRequired["capo_evs.types.environment_state_list.EnvironmentStateList"]
    """<p>The state of an environment. Used to filter response results to return only environments with the specified <code>environmentState</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentsRequest:
    out: ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    return out
