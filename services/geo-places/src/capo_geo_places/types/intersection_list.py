"""Generated from Smithy shape ``com.amazonaws.geoplaces#IntersectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.intersection

IntersectionList: TypeAlias = list["capo_geo_places.types.intersection.Intersection"]


# --- restJson1 ser/de ---
def serialize_json(value: IntersectionList) -> list:
    import capo_geo_places.types.intersection

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.intersection.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntersectionList:
    import capo_geo_places.types.intersection

    out: IntersectionList = []
    for item in data:
        out.append(capo_geo_places.types.intersection.deserialize_json(item))
    return out
