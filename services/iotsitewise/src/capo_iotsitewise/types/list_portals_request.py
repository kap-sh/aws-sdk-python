"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListPortalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListPortalsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPortalsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPortalsRequest:
    out: ListPortalsRequest = {}  # type: ignore[typeddict-item]
    return out
