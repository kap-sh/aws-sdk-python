"""Generated from Smithy shape ``com.amazonaws.fis#SafetyLeverStatus``."""

from typing import Literal, TypeAlias, cast

SafetyLeverStatus: TypeAlias = Literal[
    "disengaged",
    "engaged",
    "engaging",
]


# --- restJson1 ser/de ---
def serialize_json(value: SafetyLeverStatus) -> str:
    return value


def deserialize_json(data: str) -> SafetyLeverStatus:
    return cast(SafetyLeverStatus, data)
