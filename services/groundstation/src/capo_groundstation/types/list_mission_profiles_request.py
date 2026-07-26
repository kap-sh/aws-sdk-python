"""Generated from Smithy shape ``com.amazonaws.groundstation#ListMissionProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token


class ListMissionProfilesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of mission profiles returned.</p>"""
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token returned in the request of a previous <code>ListMissionProfiles</code> call. Used to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMissionProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMissionProfilesRequest:
    out: ListMissionProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
