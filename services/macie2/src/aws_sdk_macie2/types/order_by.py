"""Generated from Smithy shape ``com.amazonaws.macie2#OrderBy``."""

from typing import Literal, TypeAlias, cast

OrderBy: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderBy) -> str:
    return value


def deserialize_json(data: str) -> OrderBy:
    return cast(OrderBy, data)
