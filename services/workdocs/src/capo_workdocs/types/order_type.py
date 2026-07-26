"""Generated from Smithy shape ``com.amazonaws.workdocs#OrderType``."""

from typing import Literal, TypeAlias, cast

OrderType: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderType) -> str:
    return value


def deserialize_json(data: str) -> OrderType:
    return cast(OrderType, data)
