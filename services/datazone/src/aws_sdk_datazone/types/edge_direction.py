"""Generated from Smithy shape ``com.amazonaws.datazone#EdgeDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

EdgeDirection: TypeAlias = Literal[
    "UPSTREAM",
    "DOWNSTREAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPSTREAM",
        "DOWNSTREAM",
    )
)


def serialize_json(value: EdgeDirection) -> str:
    return value


def deserialize_json(data: str) -> EdgeDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EdgeDirection value: {data!r}")
    return cast(EdgeDirection, data)
