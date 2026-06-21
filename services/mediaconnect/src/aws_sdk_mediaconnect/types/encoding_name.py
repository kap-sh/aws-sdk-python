"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EncodingName``."""

from typing import Literal, TypeAlias, cast

EncodingName: TypeAlias = Literal[
    "jxsv",
    "raw",
    "smpte291",
    "pcm",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncodingName) -> str:
    return value


def deserialize_json(data: str) -> EncodingName:
    return cast(EncodingName, data)
