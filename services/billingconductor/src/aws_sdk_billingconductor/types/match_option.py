"""Generated from Smithy shape ``com.amazonaws.billingconductor#MatchOption``."""

from typing import Literal, TypeAlias, cast

MatchOption: TypeAlias = Literal[
    "NOT_EQUAL",
    "EQUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchOption) -> str:
    return value


def deserialize_json(data: str) -> MatchOption:
    return cast(MatchOption, data)
