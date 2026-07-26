"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfMediaStreamSourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.media_stream_source_configuration

__listOfMediaStreamSourceConfiguration: TypeAlias = list[
    "capo_mediaconnect.types.media_stream_source_configuration.MediaStreamSourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaStreamSourceConfiguration) -> list:
    import capo_mediaconnect.types.media_stream_source_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.media_stream_source_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfMediaStreamSourceConfiguration:
    import capo_mediaconnect.types.media_stream_source_configuration

    out: __listOfMediaStreamSourceConfiguration = []
    for item in data:
        out.append(
            capo_mediaconnect.types.media_stream_source_configuration.deserialize_json(
                item
            )
        )
    return out
