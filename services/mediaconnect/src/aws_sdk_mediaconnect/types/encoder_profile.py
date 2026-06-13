"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EncoderProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

EncoderProfile: TypeAlias = Literal[
    "main",
    "high",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "main",
        "high",
    )
)


def serialize_json(value: EncoderProfile) -> str:
    return value


def deserialize_json(data: str) -> EncoderProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncoderProfile value: {data!r}")
    return cast(EncoderProfile, data)
