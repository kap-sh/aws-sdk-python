"""Generated from Smithy shape ``com.amazonaws.quicksight#QueryExecutionMode``."""

from typing import Literal, TypeAlias, cast

QueryExecutionMode: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryExecutionMode) -> str:
    return value


def deserialize_json(data: str) -> QueryExecutionMode:
    return cast(QueryExecutionMode, data)
