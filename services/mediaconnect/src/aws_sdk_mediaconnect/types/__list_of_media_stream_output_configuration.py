"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfMediaStreamOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_stream_output_configuration

__listOfMediaStreamOutputConfiguration: TypeAlias = list[
    "aws_sdk_mediaconnect.types.media_stream_output_configuration.MediaStreamOutputConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaStreamOutputConfiguration) -> list:
    import aws_sdk_mediaconnect.types.media_stream_output_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.media_stream_output_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfMediaStreamOutputConfiguration:
    import aws_sdk_mediaconnect.types.media_stream_output_configuration

    out: __listOfMediaStreamOutputConfiguration = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.media_stream_output_configuration.deserialize_json(
                item
            )
        )
    return out
