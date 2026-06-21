"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleStatus``."""

from typing import Literal, TypeAlias, cast

BotLocaleStatus: TypeAlias = Literal[
    "Creating",
    "Building",
    "Built",
    "ReadyExpressTesting",
    "Failed",
    "Deleting",
    "NotBuilt",
    "Importing",
    "Processing",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleStatus) -> str:
    return value


def deserialize_json(data: str) -> BotLocaleStatus:
    return cast(BotLocaleStatus, data)
