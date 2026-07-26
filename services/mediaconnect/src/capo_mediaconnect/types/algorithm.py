"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Algorithm``."""

from typing import Literal, TypeAlias, cast

Algorithm: TypeAlias = Literal[
    "aes128",
    "aes192",
    "aes256",
]


# --- restJson1 ser/de ---
def serialize_json(value: Algorithm) -> str:
    return value


def deserialize_json(data: str) -> Algorithm:
    return cast(Algorithm, data)
