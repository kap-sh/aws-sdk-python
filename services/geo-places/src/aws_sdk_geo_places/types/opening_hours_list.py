"""Generated from Smithy shape ``com.amazonaws.geoplaces#OpeningHoursList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.opening_hours

OpeningHoursList: TypeAlias = list[
    "aws_sdk_geo_places.types.opening_hours.OpeningHours"
]


# --- restJson1 ser/de ---
def serialize_json(value: OpeningHoursList) -> list:
    import aws_sdk_geo_places.types.opening_hours

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_places.types.opening_hours.serialize_json(item))
    return out


def deserialize_json(data: list) -> OpeningHoursList:
    import aws_sdk_geo_places.types.opening_hours

    out: OpeningHoursList = []
    for item in data:
        out.append(aws_sdk_geo_places.types.opening_hours.deserialize_json(item))
    return out
