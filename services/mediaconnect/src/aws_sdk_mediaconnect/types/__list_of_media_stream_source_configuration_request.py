"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfMediaStreamSourceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_stream_source_configuration_request

__listOfMediaStreamSourceConfigurationRequest: TypeAlias = list[
    "aws_sdk_mediaconnect.types.media_stream_source_configuration_request.MediaStreamSourceConfigurationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaStreamSourceConfigurationRequest) -> list:
    import aws_sdk_mediaconnect.types.media_stream_source_configuration_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.media_stream_source_configuration_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfMediaStreamSourceConfigurationRequest:
    import aws_sdk_mediaconnect.types.media_stream_source_configuration_request

    out: __listOfMediaStreamSourceConfigurationRequest = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.media_stream_source_configuration_request.deserialize_json(
                item
            )
        )
    return out
