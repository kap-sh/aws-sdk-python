"""Generated from Smithy shape ``com.amazonaws.iot#ListDimensionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.max_results
    import capo_iot.types.next_token


class ListDimensionsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to retrieve at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDimensionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDimensionsRequest:
    out: ListDimensionsRequest = {}  # type: ignore[typeddict-item]
    return out
