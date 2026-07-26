"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.ground_station_name

GroundStationIdList: TypeAlias = list[
    "capo_groundstation.types.ground_station_name.GroundStationName"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroundStationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> GroundStationIdList:
    return list(data)
