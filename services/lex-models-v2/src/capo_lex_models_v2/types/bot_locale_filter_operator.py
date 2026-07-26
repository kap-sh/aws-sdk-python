"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleFilterOperator``."""

from typing import Literal, TypeAlias, cast

BotLocaleFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> BotLocaleFilterOperator:
    return cast(BotLocaleFilterOperator, data)
