"""Generated from Smithy shape ``com.amazonaws.securityhub#SeverityLabel``."""

from typing import Literal, TypeAlias, cast

SeverityLabel: TypeAlias = Literal[
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: SeverityLabel) -> str:
    return value


def deserialize_json(data: str) -> SeverityLabel:
    return cast(SeverityLabel, data)
