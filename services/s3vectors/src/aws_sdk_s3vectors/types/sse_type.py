"""Generated from Smithy shape ``com.amazonaws.s3vectors#SseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3vectors.errors import DeserializationError

SseType: TypeAlias = Literal[
    "AES256",
    "aws:kms",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES256",
        "aws:kms",
    )
)


def serialize_json(value: SseType) -> str:
    return value


def deserialize_json(data: str) -> SseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SseType value: {data!r}")
    return cast(SseType, data)
