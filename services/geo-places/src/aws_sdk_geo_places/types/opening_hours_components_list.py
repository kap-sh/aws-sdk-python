"""Generated from Smithy shape ``com.amazonaws.geoplaces#OpeningHoursComponentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.opening_hours_components

OpeningHoursComponentsList: TypeAlias = list[
    "aws_sdk_geo_places.types.opening_hours_components.OpeningHoursComponents"
]


# --- restJson1 ser/de ---
def serialize_json(value: OpeningHoursComponentsList) -> list:
    import aws_sdk_geo_places.types.opening_hours_components

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_places.types.opening_hours_components.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OpeningHoursComponentsList:
    import aws_sdk_geo_places.types.opening_hours_components

    out: OpeningHoursComponentsList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.opening_hours_components.deserialize_json(item)
        )
    return out
