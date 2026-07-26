"""Generated from Smithy shape ``com.amazonaws.groundstation#ListSatellitesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token


class ListSatellitesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of satellites returned.</p>"""
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token that can be supplied in the next call to get the next page of satellites.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSatellitesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSatellitesRequest:
    out: ListSatellitesRequest = {}  # type: ignore[typeddict-item]
    return out
