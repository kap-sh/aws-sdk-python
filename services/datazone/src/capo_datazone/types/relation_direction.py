"""Generated from Smithy shape ``com.amazonaws.datazone#RelationDirection``."""

from typing import Literal, TypeAlias, cast

RelationDirection: TypeAlias = Literal[
    "IN",
    "OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RelationDirection) -> str:
    return value


def deserialize_json(data: str) -> RelationDirection:
    return cast(RelationDirection, data)
