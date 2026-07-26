"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfMediaStreamOutputConfigurationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.media_stream_output_configuration_request

__listOfMediaStreamOutputConfigurationRequest: TypeAlias = list[
    "capo_mediaconnect.types.media_stream_output_configuration_request.MediaStreamOutputConfigurationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaStreamOutputConfigurationRequest) -> list:
    import capo_mediaconnect.types.media_stream_output_configuration_request

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.media_stream_output_configuration_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfMediaStreamOutputConfigurationRequest:
    import capo_mediaconnect.types.media_stream_output_configuration_request

    out: __listOfMediaStreamOutputConfigurationRequest = []
    for item in data:
        out.append(
            capo_mediaconnect.types.media_stream_output_configuration_request.deserialize_json(
                item
            )
        )
    return out
