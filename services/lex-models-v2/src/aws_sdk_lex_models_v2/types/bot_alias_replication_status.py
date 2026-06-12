"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>The status of the operation to replicate the bot alias. Values: Creating, Updating, Available, Deleting, Failed.</p>"""
BotAliasReplicationStatus: TypeAlias = Literal[
    "Creating",
    "Updating",
    "Available",
    "Deleting",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Updating",
        "Available",
        "Deleting",
        "Failed",
    )
)


def serialize_json(value: BotAliasReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> BotAliasReplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotAliasReplicationStatus value: {data!r}")
    return cast(BotAliasReplicationStatus, data)
