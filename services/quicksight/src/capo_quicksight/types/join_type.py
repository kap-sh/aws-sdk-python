"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinType``."""

from typing import Literal, TypeAlias, cast

JoinType: TypeAlias = Literal[
    "INNER",
    "OUTER",
    "LEFT",
    "RIGHT",
]


# --- restJson1 ser/de ---
def serialize_json(value: JoinType) -> str:
    return value


def deserialize_json(data: str) -> JoinType:
    return cast(JoinType, data)
