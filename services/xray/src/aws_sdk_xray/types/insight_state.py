"""Generated from Smithy shape ``com.amazonaws.xray#InsightState``."""

from typing import Literal, TypeAlias, cast

InsightState: TypeAlias = Literal[
    "ACTIVE",
    "CLOSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightState) -> str:
    return value


def deserialize_json(data: str) -> InsightState:
    return cast(InsightState, data)
