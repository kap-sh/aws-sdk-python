"""Generated from Smithy shape ``com.amazonaws.groundstation#ListGroundStationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.ground_station_list
    import capo_groundstation.types.pagination_token


class ListGroundStationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token that can be supplied in the next call to get the next page of ground stations.</p>"""
    ground_station_list: NotRequired[
        "capo_groundstation.types.ground_station_list.GroundStationList"
    ]
    """<p>List of ground stations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroundStationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "ground_station_list" in value:
        import capo_groundstation.types.ground_station_list

        out["groundStationList"] = (
            capo_groundstation.types.ground_station_list.serialize_json(
                value["ground_station_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListGroundStationsResponse:
    out: ListGroundStationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "groundStationList" in data:
        import capo_groundstation.types.ground_station_list

        out["ground_station_list"] = (
            capo_groundstation.types.ground_station_list.deserialize_json(
                data["groundStationList"]
            )
        )
    return out
