"""Generated from Smithy shape ``com.amazonaws.geoplaces#IntersectionStreetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.intersection_street

IntersectionStreetList: TypeAlias = list[
    "aws_sdk_geo_places.types.intersection_street.IntersectionStreet"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntersectionStreetList) -> list:
    return list(value)


def deserialize_json(data: list) -> IntersectionStreetList:
    return list(data)
