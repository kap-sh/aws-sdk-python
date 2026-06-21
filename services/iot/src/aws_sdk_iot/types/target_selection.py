"""Generated from Smithy shape ``com.amazonaws.iot#TargetSelection``."""

from typing import Literal, TypeAlias, cast

TargetSelection: TypeAlias = Literal[
    "CONTINUOUS",
    "SNAPSHOT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetSelection) -> str:
    return value


def deserialize_json(data: str) -> TargetSelection:
    return cast(TargetSelection, data)
