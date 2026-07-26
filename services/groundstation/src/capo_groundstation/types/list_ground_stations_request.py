"""Generated from Smithy shape ``com.amazonaws.groundstation#ListGroundStationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.uuid


class ListGroundStationsRequest(TypedDict, closed=True):
    satellite_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>Satellite ID to retrieve on-boarded ground stations.</p>"""
    max_results: NotRequired[
        "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of ground stations returned.</p>"""
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token that can be supplied in the next call to get the next page of ground stations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroundStationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGroundStationsRequest:
    out: ListGroundStationsRequest = {}  # type: ignore[typeddict-item]
    return out
