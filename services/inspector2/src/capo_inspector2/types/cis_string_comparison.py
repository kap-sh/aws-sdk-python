"""Generated from Smithy shape ``com.amazonaws.inspector2#CisStringComparison``."""

from typing import Literal, TypeAlias, cast

CisStringComparison: TypeAlias = Literal[
    "EQUALS",
    "PREFIX",
    "NOT_EQUALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisStringComparison) -> str:
    return value


def deserialize_json(data: str) -> CisStringComparison:
    return cast(CisStringComparison, data)
