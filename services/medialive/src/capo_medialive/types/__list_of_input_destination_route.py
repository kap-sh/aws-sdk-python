"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDestinationRoute``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_destination_route

__listOfInputDestinationRoute: TypeAlias = list[
    "capo_medialive.types.input_destination_route.InputDestinationRoute"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDestinationRoute) -> list:
    import capo_medialive.types.input_destination_route

    out: list = []
    for item in value:
        out.append(capo_medialive.types.input_destination_route.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputDestinationRoute:
    import capo_medialive.types.input_destination_route

    out: __listOfInputDestinationRoute = []
    for item in data:
        out.append(capo_medialive.types.input_destination_route.deserialize_json(item))
    return out
