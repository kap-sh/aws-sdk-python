"""Generated from Smithy shape ``com.amazonaws.batch#CEState``."""

from typing import Literal, TypeAlias, cast

CEState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CEState) -> str:
    return value


def deserialize_json(data: str) -> CEState:
    return cast(CEState, data)
