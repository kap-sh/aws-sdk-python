"""Generated from Smithy shape ``com.amazonaws.iot#FleetIndexingApiList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.fleet_indexing_api

FleetIndexingApiList: TypeAlias = list[
    "capo_iot.types.fleet_indexing_api.FleetIndexingApi"
]


# --- restJson1 ser/de ---
def serialize_json(value: FleetIndexingApiList) -> list:
    import capo_iot.types.fleet_indexing_api

    out: list = []
    for item in value:
        out.append(capo_iot.types.fleet_indexing_api.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetIndexingApiList:
    import capo_iot.types.fleet_indexing_api

    out: FleetIndexingApiList = []
    for item in data:
        out.append(capo_iot.types.fleet_indexing_api.deserialize_json(item))
    return out
