"""Generated from Smithy shape ``com.amazonaws.geomaps#TravelModeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_maps.types.travel_mode

TravelModeList: TypeAlias = list["capo_geo_maps.types.travel_mode.TravelMode"]


# --- restJson1 ser/de ---
def serialize_json(value: TravelModeList) -> list:
    return list(value)


def deserialize_json(data: list) -> TravelModeList:
    return list(data)
