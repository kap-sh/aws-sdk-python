"""Generated from Smithy shape ``com.amazonaws.securityir#ClosureCode``."""

from typing import Literal, TypeAlias, cast

ClosureCode: TypeAlias = Literal[
    "Investigation Completed",
    "Not Resolved",
    "False Positive",
    "Duplicate",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClosureCode) -> str:
    return value


def deserialize_json(data: str) -> ClosureCode:
    return cast(ClosureCode, data)
