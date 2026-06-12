"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfPlaybackConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.playback_configuration

__listOfPlaybackConfiguration: TypeAlias = list[
    "aws_sdk_mediatailor.types.playback_configuration.PlaybackConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPlaybackConfiguration) -> list:
    import aws_sdk_mediatailor.types.playback_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediatailor.types.playback_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfPlaybackConfiguration:
    import aws_sdk_mediatailor.types.playback_configuration

    out: __listOfPlaybackConfiguration = []
    for item in data:
        out.append(
            aws_sdk_mediatailor.types.playback_configuration.deserialize_json(item)
        )
    return out
