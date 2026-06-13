"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfMediaStreamOutputConfigurationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_stream_output_configuration_request

__listOfMediaStreamOutputConfigurationRequest: TypeAlias = list[
    "aws_sdk_mediaconnect.types.media_stream_output_configuration_request.MediaStreamOutputConfigurationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaStreamOutputConfigurationRequest) -> list:
    import aws_sdk_mediaconnect.types.media_stream_output_configuration_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.media_stream_output_configuration_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfMediaStreamOutputConfigurationRequest:
    import aws_sdk_mediaconnect.types.media_stream_output_configuration_request

    out: __listOfMediaStreamOutputConfigurationRequest = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.media_stream_output_configuration_request.deserialize_json(
                item
            )
        )
    return out
