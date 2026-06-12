"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>The status of the operation to replicate the bot version. Values: Creating, Available, Deleting, Failed.</p>"""
BotVersionReplicationStatus: TypeAlias = Literal[
    "Creating",
    "Available",
    "Deleting",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Available",
        "Deleting",
        "Failed",
    )
)


def serialize_json(value: BotVersionReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> BotVersionReplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BotVersionReplicationStatus value: {data!r}"
        )
    return cast(BotVersionReplicationStatus, data)
