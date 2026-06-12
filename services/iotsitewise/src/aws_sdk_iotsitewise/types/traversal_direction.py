"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TraversalDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

TraversalDirection: TypeAlias = Literal[
    "PARENT",
    "CHILD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARENT",
        "CHILD",
    )
)


def serialize_json(value: TraversalDirection) -> str:
    return value


def deserialize_json(data: str) -> TraversalDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TraversalDirection value: {data!r}")
    return cast(TraversalDirection, data)
