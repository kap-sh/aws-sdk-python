"""Generated from Smithy shape ``com.amazonaws.outposts#OrderType``."""

from typing import Literal, TypeAlias, cast

OrderType: TypeAlias = Literal[
    "OUTPOST",
    "REPLACEMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderType) -> str:
    return value


def deserialize_json(data: str) -> OrderType:
    return cast(OrderType, data)
