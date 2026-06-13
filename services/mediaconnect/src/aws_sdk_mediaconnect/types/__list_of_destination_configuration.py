"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfDestinationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.destination_configuration

__listOfDestinationConfiguration: TypeAlias = list[
    "aws_sdk_mediaconnect.types.destination_configuration.DestinationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDestinationConfiguration) -> list:
    import aws_sdk_mediaconnect.types.destination_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.destination_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfDestinationConfiguration:
    import aws_sdk_mediaconnect.types.destination_configuration

    out: __listOfDestinationConfiguration = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.destination_configuration.deserialize_json(item)
        )
    return out
