"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareState``."""

from typing import Literal, TypeAlias, cast

QuotaShareState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareState) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareState:
    return cast(QuotaShareState, data)
