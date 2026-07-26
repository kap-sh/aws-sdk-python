"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotReplicaStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the operation to replicate the bot. Values: Enabling, Enabled, Deleting, Failed.</p>"""
BotReplicaStatus: TypeAlias = Literal[
    "Enabling",
    "Enabled",
    "Deleting",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotReplicaStatus) -> str:
    return value


def deserialize_json(data: str) -> BotReplicaStatus:
    return cast(BotReplicaStatus, data)
