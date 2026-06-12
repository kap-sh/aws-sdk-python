"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

NodeType: TypeAlias = Literal[
    "Data",
    "Ultrawarm",
    "Master",
    "Warm",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Data",
        "Ultrawarm",
        "Master",
        "Warm",
    )
)


def serialize_json(value: NodeType) -> str:
    return value


def deserialize_json(data: str) -> NodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeType value: {data!r}")
    return cast(NodeType, data)
