"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#LocationStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.location_state

LocationStates: TypeAlias = list[
    "aws_sdk_gameliftstreams.types.location_state.LocationState"
]


# --- restJson1 ser/de ---
def serialize_json(value: LocationStates) -> list:
    import aws_sdk_gameliftstreams.types.location_state

    out: list = []
    for item in value:
        out.append(aws_sdk_gameliftstreams.types.location_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> LocationStates:
    import aws_sdk_gameliftstreams.types.location_state

    out: LocationStates = []
    for item in data:
        out.append(aws_sdk_gameliftstreams.types.location_state.deserialize_json(item))
    return out
