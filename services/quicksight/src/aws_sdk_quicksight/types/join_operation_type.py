"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinOperationType``."""

from typing import Literal, TypeAlias, cast

JoinOperationType: TypeAlias = Literal[
    "INNER",
    "OUTER",
    "LEFT",
    "RIGHT",
]


# --- restJson1 ser/de ---
def serialize_json(value: JoinOperationType) -> str:
    return value


def deserialize_json(data: str) -> JoinOperationType:
    return cast(JoinOperationType, data)
