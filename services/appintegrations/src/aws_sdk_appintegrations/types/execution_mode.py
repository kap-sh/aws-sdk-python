"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExecutionMode``."""

from typing import Literal, TypeAlias, cast

ExecutionMode: TypeAlias = Literal[
    "ON_DEMAND",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionMode) -> str:
    return value


def deserialize_json(data: str) -> ExecutionMode:
    return cast(ExecutionMode, data)
