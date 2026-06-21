"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipTarget``."""

from typing import Literal, TypeAlias, cast

TooltipTarget: TypeAlias = Literal[
    "BOTH",
    "BAR",
    "LINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipTarget) -> str:
    return value


def deserialize_json(data: str) -> TooltipTarget:
    return cast(TooltipTarget, data)
