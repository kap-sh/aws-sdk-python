"""Generated from Smithy shape ``com.amazonaws.geoplaces#StreetComponentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.street_components

StreetComponentsList: TypeAlias = list[
    "aws_sdk_geo_places.types.street_components.StreetComponents"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreetComponentsList) -> list:
    import aws_sdk_geo_places.types.street_components

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_places.types.street_components.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreetComponentsList:
    import aws_sdk_geo_places.types.street_components

    out: StreetComponentsList = []
    for item in data:
        out.append(aws_sdk_geo_places.types.street_components.deserialize_json(item))
    return out
