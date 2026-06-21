"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotStatus``."""

from typing import Literal, TypeAlias, cast

BotStatus: TypeAlias = Literal[
    "Creating",
    "Available",
    "Inactive",
    "Deleting",
    "Failed",
    "Versioning",
    "Importing",
    "Updating",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotStatus) -> str:
    return value


def deserialize_json(data: str) -> BotStatus:
    return cast(BotStatus, data)
