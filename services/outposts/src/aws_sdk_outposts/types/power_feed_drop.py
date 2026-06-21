"""Generated from Smithy shape ``com.amazonaws.outposts#PowerFeedDrop``."""

from typing import Literal, TypeAlias, cast

PowerFeedDrop: TypeAlias = Literal[
    "ABOVE_RACK",
    "BELOW_RACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: PowerFeedDrop) -> str:
    return value


def deserialize_json(data: str) -> PowerFeedDrop:
    return cast(PowerFeedDrop, data)
