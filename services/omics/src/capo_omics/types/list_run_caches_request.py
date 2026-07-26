"""Generated from Smithy shape ``com.amazonaws.omics#ListRunCachesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.list_token


class ListRunCachesRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return.</p>"""
    starting_token: NotRequired["capo_omics.types.list_token.ListToken"]
    """<p>Optional pagination token returned from a prior call to the <code>ListRunCaches</code> API operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunCachesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRunCachesRequest:
    out: ListRunCachesRequest = {}  # type: ignore[typeddict-item]
    return out
