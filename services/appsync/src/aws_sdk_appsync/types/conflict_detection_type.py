"""Generated from Smithy shape ``com.amazonaws.appsync#ConflictDetectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

ConflictDetectionType: TypeAlias = Literal[
    "VERSION",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERSION",
        "NONE",
    )
)


def serialize_json(value: ConflictDetectionType) -> str:
    return value


def deserialize_json(data: str) -> ConflictDetectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictDetectionType value: {data!r}")
    return cast(ConflictDetectionType, data)
