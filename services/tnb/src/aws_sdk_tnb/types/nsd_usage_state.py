"""Generated from Smithy shape ``com.amazonaws.tnb#NsdUsageState``."""

from typing import Literal, TypeAlias, cast

NsdUsageState: TypeAlias = Literal[
    "IN_USE",
    "NOT_IN_USE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NsdUsageState) -> str:
    return value


def deserialize_json(data: str) -> NsdUsageState:
    return cast(NsdUsageState, data)
