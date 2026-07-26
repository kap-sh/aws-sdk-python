"""Generated from Smithy shape ``com.amazonaws.deadline#CompletedStatus``."""

from typing import Literal, TypeAlias, cast

CompletedStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "INTERRUPTED",
    "CANCELED",
    "NEVER_ATTEMPTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CompletedStatus) -> str:
    return value


def deserialize_json(data: str) -> CompletedStatus:
    return cast(CompletedStatus, data)
