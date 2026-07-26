"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeFilterPlaceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.reverse_geocode_filter_place_type

ReverseGeocodeFilterPlaceTypeList: TypeAlias = list[
    "capo_geo_places.types.reverse_geocode_filter_place_type.ReverseGeocodeFilterPlaceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeFilterPlaceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ReverseGeocodeFilterPlaceTypeList:
    return list(data)
