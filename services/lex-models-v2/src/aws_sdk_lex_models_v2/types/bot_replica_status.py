"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotReplicaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>The status of the operation to replicate the bot. Values: Enabling, Enabled, Deleting, Failed.</p>"""
BotReplicaStatus: TypeAlias = Literal[
    "Enabling",
    "Enabled",
    "Deleting",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabling",
        "Enabled",
        "Deleting",
        "Failed",
    )
)


def serialize_json(value: BotReplicaStatus) -> str:
    return value


def deserialize_json(data: str) -> BotReplicaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotReplicaStatus value: {data!r}")
    return cast(BotReplicaStatus, data)
