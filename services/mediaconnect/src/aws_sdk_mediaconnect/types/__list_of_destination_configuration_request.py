"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfDestinationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.destination_configuration_request

__listOfDestinationConfigurationRequest: TypeAlias = list[
    "aws_sdk_mediaconnect.types.destination_configuration_request.DestinationConfigurationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDestinationConfigurationRequest) -> list:
    import aws_sdk_mediaconnect.types.destination_configuration_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.destination_configuration_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfDestinationConfigurationRequest:
    import aws_sdk_mediaconnect.types.destination_configuration_request

    out: __listOfDestinationConfigurationRequest = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.destination_configuration_request.deserialize_json(
                item
            )
        )
    return out
