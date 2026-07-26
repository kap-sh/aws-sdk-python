"""Generated from Smithy shape ``com.amazonaws.networkmonitor#ListMonitorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmonitor.types.max_results
    import capo_networkmonitor.types.pagination_token


class ListMonitorsInput(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_networkmonitor.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_networkmonitor.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    state: NotRequired["str"]
    """<p>The list of all monitors and their states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMonitorsInput:
    out: ListMonitorsInput = {}  # type: ignore[typeddict-item]
    return out
