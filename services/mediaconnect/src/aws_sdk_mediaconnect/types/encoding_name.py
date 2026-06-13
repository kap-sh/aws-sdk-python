"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EncodingName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

EncodingName: TypeAlias = Literal[
    "jxsv",
    "raw",
    "smpte291",
    "pcm",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "jxsv",
        "raw",
        "smpte291",
        "pcm",
    )
)


def serialize_json(value: EncodingName) -> str:
    return value


def deserialize_json(data: str) -> EncodingName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncodingName value: {data!r}")
    return cast(EncodingName, data)
