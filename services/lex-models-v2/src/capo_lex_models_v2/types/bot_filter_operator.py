"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotFilterOperator``."""

from typing import Literal, TypeAlias, cast

BotFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
    "NE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> BotFilterOperator:
    return cast(BotFilterOperator, data)
