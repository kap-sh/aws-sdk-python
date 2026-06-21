"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AudioFormat``."""

from typing import Literal, TypeAlias, cast

AudioFormat: TypeAlias = Literal[
    "mp3",
    "opus",
    "wav",
    "aac",
    "flac",
    "mp4",
    "ogg",
    "mkv",
    "mka",
    "x-aac",
    "m4a",
    "mpeg",
    "mpga",
    "pcm",
    "webm",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioFormat) -> str:
    return value


def deserialize_json(data: str) -> AudioFormat:
    return cast(AudioFormat, data)
