"""Generated from Smithy shape ``com.amazonaws.auditmanager#SourceFrequency``."""

from typing import Literal, TypeAlias, cast

SourceFrequency: TypeAlias = Literal[
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceFrequency) -> str:
    return value


def deserialize_json(data: str) -> SourceFrequency:
    return cast(SourceFrequency, data)
