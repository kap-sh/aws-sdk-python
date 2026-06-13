"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Algorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

Algorithm: TypeAlias = Literal[
    "aes128",
    "aes192",
    "aes256",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "aes128",
        "aes192",
        "aes256",
    )
)


def serialize_json(value: Algorithm) -> str:
    return value


def deserialize_json(data: str) -> Algorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Algorithm value: {data!r}")
    return cast(Algorithm, data)
