"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightSeverity``."""

from typing import Literal, TypeAlias, cast

InsightSeverity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightSeverity) -> str:
    return value


def deserialize_json(data: str) -> InsightSeverity:
    return cast(InsightSeverity, data)
