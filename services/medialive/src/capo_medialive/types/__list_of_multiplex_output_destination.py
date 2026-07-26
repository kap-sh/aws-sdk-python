"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMultiplexOutputDestination``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.multiplex_output_destination

__listOfMultiplexOutputDestination: TypeAlias = list[
    "capo_medialive.types.multiplex_output_destination.MultiplexOutputDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMultiplexOutputDestination) -> list:
    import capo_medialive.types.multiplex_output_destination

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.multiplex_output_destination.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfMultiplexOutputDestination:
    import capo_medialive.types.multiplex_output_destination

    out: __listOfMultiplexOutputDestination = []
    for item in data:
        out.append(
            capo_medialive.types.multiplex_output_destination.deserialize_json(item)
        )
    return out
