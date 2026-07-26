"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MediaEncoding``."""

from typing import Literal, TypeAlias, cast

MediaEncoding: TypeAlias = Literal[
    "pcm",
    "ogg-opus",
    "flac",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaEncoding) -> str:
    return value


def deserialize_json(data: str) -> MediaEncoding:
    return cast(MediaEncoding, data)
