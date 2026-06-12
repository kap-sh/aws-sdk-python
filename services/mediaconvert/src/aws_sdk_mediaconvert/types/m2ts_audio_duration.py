"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsAudioDuration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec."""
M2tsAudioDuration: TypeAlias = Literal[
    "DEFAULT_CODEC_DURATION",
    "MATCH_VIDEO_DURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT_CODEC_DURATION",
        "MATCH_VIDEO_DURATION",
    )
)


def serialize_json(value: M2tsAudioDuration) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioDuration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsAudioDuration value: {data!r}")
    return cast(M2tsAudioDuration, data)
