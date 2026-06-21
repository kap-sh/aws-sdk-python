"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasReplicationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the operation to replicate the bot alias. Values: Creating, Updating, Available, Deleting, Failed.</p>"""
BotAliasReplicationStatus: TypeAlias = Literal[
    "Creating",
    "Updating",
    "Available",
    "Deleting",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> BotAliasReplicationStatus:
    return cast(BotAliasReplicationStatus, data)
