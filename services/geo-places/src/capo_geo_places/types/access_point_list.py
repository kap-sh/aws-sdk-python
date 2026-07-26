"""Generated from Smithy shape ``com.amazonaws.geoplaces#AccessPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.access_point

AccessPointList: TypeAlias = list["capo_geo_places.types.access_point.AccessPoint"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPointList) -> list:
    import capo_geo_places.types.access_point

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.access_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessPointList:
    import capo_geo_places.types.access_point

    out: AccessPointList = []
    for item in data:
        out.append(capo_geo_places.types.access_point.deserialize_json(item))
    return out
