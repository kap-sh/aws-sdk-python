"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ConsistencyLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

ConsistencyLevel: TypeAlias = Literal[
    "SERIALIZABLE",
    "EVENTUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERIALIZABLE",
        "EVENTUAL",
    )
)


def serialize_json(value: ConsistencyLevel) -> str:
    return value


def deserialize_json(data: str) -> ConsistencyLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConsistencyLevel value: {data!r}")
    return cast(ConsistencyLevel, data)
