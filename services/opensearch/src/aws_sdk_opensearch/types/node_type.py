"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeType``."""

from typing import Literal, TypeAlias, cast

NodeType: TypeAlias = Literal[
    "Data",
    "Ultrawarm",
    "Master",
    "Warm",
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeType) -> str:
    return value


def deserialize_json(data: str) -> NodeType:
    return cast(NodeType, data)
