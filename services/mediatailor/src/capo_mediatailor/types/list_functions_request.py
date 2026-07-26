"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListFunctionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.max_results


class ListFunctionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_mediatailor.types.max_results.MaxResults"]
    """<p>The maximum number of functions that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> functions, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses token-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>"""
    next_token: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListFunctions</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionsRequest:
    out: ListFunctionsRequest = {}  # type: ignore[typeddict-item]
    return out
