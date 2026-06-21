"""Generated from Smithy shape ``com.amazonaws.datazone#RuleScopeSelectionMode``."""

from typing import Literal, TypeAlias, cast

RuleScopeSelectionMode: TypeAlias = Literal[
    "ALL",
    "SPECIFIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleScopeSelectionMode) -> str:
    return value


def deserialize_json(data: str) -> RuleScopeSelectionMode:
    return cast(RuleScopeSelectionMode, data)
