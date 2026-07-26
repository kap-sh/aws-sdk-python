"""Generated from Smithy shape ``com.amazonaws.groundstation#ListEphemeridesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.ephemerides_list
    import capo_groundstation.types.pagination_token


class ListEphemeridesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Pagination token.</p>"""
    ephemerides: NotRequired[
        "capo_groundstation.types.ephemerides_list.EphemeridesList"
    ]
    """<p>List of ephemerides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEphemeridesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "ephemerides" in value:
        import capo_groundstation.types.ephemerides_list

        out["ephemerides"] = capo_groundstation.types.ephemerides_list.serialize_json(
            value["ephemerides"]
        )
    return out


def deserialize_json(data: dict) -> ListEphemeridesResponse:
    out: ListEphemeridesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "ephemerides" in data:
        import capo_groundstation.types.ephemerides_list

        out["ephemerides"] = capo_groundstation.types.ephemerides_list.deserialize_json(
            data["ephemerides"]
        )
    return out
