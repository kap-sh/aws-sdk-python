"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeFilterPlaceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.geocode_filter_place_type

GeocodeFilterPlaceTypeList: TypeAlias = list[
    "capo_geo_places.types.geocode_filter_place_type.GeocodeFilterPlaceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeFilterPlaceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> GeocodeFilterPlaceTypeList:
    return list(data)
