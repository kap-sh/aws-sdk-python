"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StrategyOnFullSize``."""

from typing import Literal, TypeAlias, cast

StrategyOnFullSize: TypeAlias = Literal[
    "DELETE_OLDEST_MEDIA",
    "DENY_NEW_MEDIA",
]


# --- restJson1 ser/de ---
def serialize_json(value: StrategyOnFullSize) -> str:
    return value


def deserialize_json(data: str) -> StrategyOnFullSize:
    return cast(StrategyOnFullSize, data)
