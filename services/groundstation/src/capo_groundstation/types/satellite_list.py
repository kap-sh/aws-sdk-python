"""Generated from Smithy shape ``com.amazonaws.groundstation#SatelliteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.satellite_list_item

SatelliteList: TypeAlias = list[
    "capo_groundstation.types.satellite_list_item.SatelliteListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SatelliteList) -> list:
    import capo_groundstation.types.satellite_list_item

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.satellite_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SatelliteList:
    import capo_groundstation.types.satellite_list_item

    out: SatelliteList = []
    for item in data:
        out.append(capo_groundstation.types.satellite_list_item.deserialize_json(item))
    return out
