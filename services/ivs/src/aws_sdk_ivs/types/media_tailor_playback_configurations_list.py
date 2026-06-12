"""Generated from Smithy shape ``com.amazonaws.ivs#MediaTailorPlaybackConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.media_tailor_playback_configuration

MediaTailorPlaybackConfigurationsList: TypeAlias = list[
    "aws_sdk_ivs.types.media_tailor_playback_configuration.MediaTailorPlaybackConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaTailorPlaybackConfigurationsList) -> list:
    import aws_sdk_ivs.types.media_tailor_playback_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs.types.media_tailor_playback_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MediaTailorPlaybackConfigurationsList:
    import aws_sdk_ivs.types.media_tailor_playback_configuration

    out: MediaTailorPlaybackConfigurationsList = []
    for item in data:
        out.append(
            aws_sdk_ivs.types.media_tailor_playback_configuration.deserialize_json(item)
        )
    return out
