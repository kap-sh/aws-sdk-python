"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotAliasStatus: TypeAlias = Literal[
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


def serialize_json(value: BotAliasStatus) -> str:
    return value


def deserialize_json(data: str) -> BotAliasStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotAliasStatus value: {data!r}")
    return cast(BotAliasStatus, data)
