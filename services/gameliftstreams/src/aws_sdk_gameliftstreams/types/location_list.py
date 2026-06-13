"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#LocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.location_name

LocationList: TypeAlias = list[
    "aws_sdk_gameliftstreams.types.location_name.LocationName"
]


# --- restJson1 ser/de ---
def serialize_json(value: LocationList) -> list:
    return list(value)


def deserialize_json(data: list) -> LocationList:
    return list(data)
