"""Generated from Smithy shape ``com.amazonaws.securityhub#SeverityRating``."""

from typing import Literal, TypeAlias, cast

SeverityRating: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: SeverityRating) -> str:
    return value


def deserialize_json(data: str) -> SeverityRating:
    return cast(SeverityRating, data)
