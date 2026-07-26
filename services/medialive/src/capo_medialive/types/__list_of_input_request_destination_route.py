"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputRequestDestinationRoute``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_request_destination_route

__listOfInputRequestDestinationRoute: TypeAlias = list[
    "capo_medialive.types.input_request_destination_route.InputRequestDestinationRoute"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputRequestDestinationRoute) -> list:
    import capo_medialive.types.input_request_destination_route

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.input_request_destination_route.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfInputRequestDestinationRoute:
    import capo_medialive.types.input_request_destination_route

    out: __listOfInputRequestDestinationRoute = []
    for item in data:
        out.append(
            capo_medialive.types.input_request_destination_route.deserialize_json(item)
        )
    return out
