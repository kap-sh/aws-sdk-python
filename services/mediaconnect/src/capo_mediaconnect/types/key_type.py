"""Generated from Smithy shape ``com.amazonaws.mediaconnect#KeyType``."""

from typing import Literal, TypeAlias, cast

KeyType: TypeAlias = Literal[
    "speke",
    "static-key",
    "srt-password",
]


# --- restJson1 ser/de ---
def serialize_json(value: KeyType) -> str:
    return value


def deserialize_json(data: str) -> KeyType:
    return cast(KeyType, data)
