"""Generated from Smithy shape ``com.amazonaws.eks#WarmPoolState``."""

from typing import Literal, TypeAlias, cast

WarmPoolState: TypeAlias = Literal[
    "STOPPED",
    "RUNNING",
    "HIBERNATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WarmPoolState) -> str:
    return value


def deserialize_json(data: str) -> WarmPoolState:
    return cast(WarmPoolState, data)
