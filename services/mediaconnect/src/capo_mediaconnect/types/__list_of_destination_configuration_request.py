"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfDestinationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_configuration_request

__listOfDestinationConfigurationRequest: TypeAlias = list[
    "capo_mediaconnect.types.destination_configuration_request.DestinationConfigurationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDestinationConfigurationRequest) -> list:
    import capo_mediaconnect.types.destination_configuration_request

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.destination_configuration_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfDestinationConfigurationRequest:
    import capo_mediaconnect.types.destination_configuration_request

    out: __listOfDestinationConfigurationRequest = []
    for item in data:
        out.append(
            capo_mediaconnect.types.destination_configuration_request.deserialize_json(
                item
            )
        )
    return out
