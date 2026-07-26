"""Generated from Smithy shape ``com.amazonaws.iot#ListIndicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.query_max_results


class ListIndicesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token used to get the next set of results, or <code>null</code> if there are no additional results.</p>"""
    max_results: NotRequired["capo_iot.types.query_max_results.QueryMaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIndicesRequest:
    out: ListIndicesRequest = {}  # type: ignore[typeddict-item]
    return out
