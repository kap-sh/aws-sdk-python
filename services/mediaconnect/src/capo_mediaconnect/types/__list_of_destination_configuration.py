"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfDestinationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_configuration

__listOfDestinationConfiguration: TypeAlias = list[
    "capo_mediaconnect.types.destination_configuration.DestinationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDestinationConfiguration) -> list:
    import capo_mediaconnect.types.destination_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.destination_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfDestinationConfiguration:
    import capo_mediaconnect.types.destination_configuration

    out: __listOfDestinationConfiguration = []
    for item in data:
        out.append(
            capo_mediaconnect.types.destination_configuration.deserialize_json(item)
        )
    return out
