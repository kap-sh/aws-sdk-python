"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaEncoding``."""

from typing import Literal, TypeAlias, cast

MediaEncoding: TypeAlias = Literal["pcm",]


# --- restJson1 ser/de ---
def serialize_json(value: MediaEncoding) -> str:
    return value


def deserialize_json(data: str) -> MediaEncoding:
    return cast(MediaEncoding, data)
