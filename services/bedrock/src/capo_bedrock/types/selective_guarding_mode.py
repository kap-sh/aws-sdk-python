"""Generated from Smithy shape ``com.amazonaws.bedrock#SelectiveGuardingMode``."""

from typing import Literal, TypeAlias, cast

SelectiveGuardingMode: TypeAlias = Literal[
    "SELECTIVE",
    "COMPREHENSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SelectiveGuardingMode) -> str:
    return value


def deserialize_json(data: str) -> SelectiveGuardingMode:
    return cast(SelectiveGuardingMode, data)
