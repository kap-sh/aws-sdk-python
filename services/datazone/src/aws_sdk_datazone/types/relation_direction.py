"""Generated from Smithy shape ``com.amazonaws.datazone#RelationDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

RelationDirection: TypeAlias = Literal[
    "IN",
    "OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN",
        "OUT",
    )
)


def serialize_json(value: RelationDirection) -> str:
    return value


def deserialize_json(data: str) -> RelationDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelationDirection value: {data!r}")
    return cast(RelationDirection, data)
