"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasStatus``."""

from typing import Literal, TypeAlias, cast

BotAliasStatus: TypeAlias = Literal[
    "Creating",
    "Available",
    "Deleting",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasStatus) -> str:
    return value


def deserialize_json(data: str) -> BotAliasStatus:
    return cast(BotAliasStatus, data)
