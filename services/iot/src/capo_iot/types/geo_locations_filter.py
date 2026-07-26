"""Generated from Smithy shape ``com.amazonaws.iot#GeoLocationsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.geo_location_target

GeoLocationsFilter: TypeAlias = list[
    "capo_iot.types.geo_location_target.GeoLocationTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeoLocationsFilter) -> list:
    import capo_iot.types.geo_location_target

    out: list = []
    for item in value:
        out.append(capo_iot.types.geo_location_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> GeoLocationsFilter:
    import capo_iot.types.geo_location_target

    out: GeoLocationsFilter = []
    for item in data:
        out.append(capo_iot.types.geo_location_target.deserialize_json(item))
    return out
