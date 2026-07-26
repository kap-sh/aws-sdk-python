"""Generated from Smithy shape ``com.amazonaws.geoplaces#RelatedPlaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.related_place

RelatedPlaceList: TypeAlias = list["capo_geo_places.types.related_place.RelatedPlace"]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedPlaceList) -> list:
    import capo_geo_places.types.related_place

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.related_place.serialize_json(item))
    return out


def deserialize_json(data: list) -> RelatedPlaceList:
    import capo_geo_places.types.related_place

    out: RelatedPlaceList = []
    for item in data:
        out.append(capo_geo_places.types.related_place.deserialize_json(item))
    return out
