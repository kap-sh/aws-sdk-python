"""Generated from Smithy shape ``com.amazonaws.controltower#ListLandingZonesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.list_landing_zones_max_results


class ListLandingZonesInput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to continue the list from a previous API call with the same parameters.</p>"""
    max_results: NotRequired[
        "capo_controltower.types.list_landing_zones_max_results.ListLandingZonesMaxResults"
    ]
    """<p>The maximum number of returned landing zone ARNs, which is one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLandingZonesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListLandingZonesInput:
    out: ListLandingZonesInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
