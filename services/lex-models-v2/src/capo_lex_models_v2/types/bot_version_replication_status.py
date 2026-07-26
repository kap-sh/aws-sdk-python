"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionReplicationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the operation to replicate the bot version. Values: Creating, Available, Deleting, Failed.</p>"""
BotVersionReplicationStatus: TypeAlias = Literal[
    "Creating",
    "Available",
    "Deleting",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> BotVersionReplicationStatus:
    return cast(BotVersionReplicationStatus, data)
