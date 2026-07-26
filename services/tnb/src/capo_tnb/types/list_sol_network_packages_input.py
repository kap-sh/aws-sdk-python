"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkPackagesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.pagination_token


class ListSolNetworkPackagesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response.</p>"""
    next_token: NotRequired["capo_tnb.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkPackagesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSolNetworkPackagesInput:
    out: ListSolNetworkPackagesInput = {}  # type: ignore[typeddict-item]
    return out
