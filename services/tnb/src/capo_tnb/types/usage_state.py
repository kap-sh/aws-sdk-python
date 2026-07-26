"""Generated from Smithy shape ``com.amazonaws.tnb#UsageState``."""

from typing import Literal, TypeAlias, cast

UsageState: TypeAlias = Literal[
    "IN_USE",
    "NOT_IN_USE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageState) -> str:
    return value


def deserialize_json(data: str) -> UsageState:
    return cast(UsageState, data)
