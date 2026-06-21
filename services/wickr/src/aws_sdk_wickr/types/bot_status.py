"""Generated from Smithy shape ``com.amazonaws.wickr#BotStatus``."""

from typing import Literal, TypeAlias, cast

BotStatus: TypeAlias = Literal[
    1,
    2,
]


# --- restJson1 ser/de ---
def serialize_json(value: BotStatus) -> int:
    return value


def deserialize_json(data: int) -> BotStatus:
    return cast(BotStatus, data)
