"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#LocationStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gameliftstreams.types.location_state

LocationStates: TypeAlias = list[
    "capo_gameliftstreams.types.location_state.LocationState"
]


# --- restJson1 ser/de ---
def serialize_json(value: LocationStates) -> list:
    import capo_gameliftstreams.types.location_state

    out: list = []
    for item in value:
        out.append(capo_gameliftstreams.types.location_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> LocationStates:
    import capo_gameliftstreams.types.location_state

    out: LocationStates = []
    for item in data:
        out.append(capo_gameliftstreams.types.location_state.deserialize_json(item))
    return out
