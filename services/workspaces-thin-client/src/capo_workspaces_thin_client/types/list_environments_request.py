"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ListEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.max_results
    import capo_workspaces_thin_client.types.pagination_token


class ListEnvironmentsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_workspaces_thin_client.types.pagination_token.PaginationToken"
    ]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""
    max_results: NotRequired["capo_workspaces_thin_client.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentsRequest:
    out: ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    return out
