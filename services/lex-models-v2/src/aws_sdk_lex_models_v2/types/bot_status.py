"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Available",
        "Inactive",
        "Deleting",
        "Failed",
        "Versioning",
        "Importing",
        "Updating",
    )
)


def serialize_json(value: BotStatus) -> str:
    return value


def deserialize_json(data: str) -> BotStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotStatus value: {data!r}")
    return cast(BotStatus, data)
