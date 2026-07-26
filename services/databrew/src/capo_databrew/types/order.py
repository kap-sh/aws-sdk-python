"""Generated from Smithy shape ``com.amazonaws.databrew#Order``."""

from typing import Literal, TypeAlias, cast

Order: TypeAlias = Literal[
    "DESCENDING",
    "ASCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: Order) -> str:
    return value


def deserialize_json(data: str) -> Order:
    return cast(Order, data)
