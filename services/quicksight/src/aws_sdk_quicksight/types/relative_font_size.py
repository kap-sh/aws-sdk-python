"""Generated from Smithy shape ``com.amazonaws.quicksight#RelativeFontSize``."""

from typing import Literal, TypeAlias, cast

RelativeFontSize: TypeAlias = Literal[
    "EXTRA_SMALL",
    "SMALL",
    "MEDIUM",
    "LARGE",
    "EXTRA_LARGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RelativeFontSize) -> str:
    return value


def deserialize_json(data: str) -> RelativeFontSize:
    return cast(RelativeFontSize, data)
