"""Generated from Smithy shape ``com.amazonaws.polly#OutputFormat``."""

from typing import Literal, TypeAlias, cast

OutputFormat: TypeAlias = Literal[
    "json",
    "mp3",
    "ogg_opus",
    "ogg_vorbis",
    "pcm",
    "mulaw",
    "alaw",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    return cast(OutputFormat, data)
