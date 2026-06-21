"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FindingSeverity``."""

from typing import Literal, TypeAlias, cast

FindingSeverity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingSeverity) -> str:
    return value


def deserialize_json(data: str) -> FindingSeverity:
    return cast(FindingSeverity, data)
