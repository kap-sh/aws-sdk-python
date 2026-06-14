"""Generated from Smithy shape ``com.amazonaws.datazone#S3Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

S3Permission: TypeAlias = Literal[
    "READ",
    "WRITE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "WRITE",
    )
)


def serialize_json(value: S3Permission) -> str:
    return value


def deserialize_json(data: str) -> S3Permission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3Permission value: {data!r}")
    return cast(S3Permission, data)
