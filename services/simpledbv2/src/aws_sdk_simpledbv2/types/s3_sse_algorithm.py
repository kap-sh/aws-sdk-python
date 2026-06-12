"""Generated from Smithy shape ``com.amazonaws.simpledbv2#S3SseAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_simpledbv2.errors import DeserializationError

S3SseAlgorithm: TypeAlias = Literal[
    "AES256",
    "KMS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES256",
        "KMS",
    )
)


def serialize_json(value: S3SseAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> S3SseAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3SseAlgorithm value: {data!r}")
    return cast(S3SseAlgorithm, data)
