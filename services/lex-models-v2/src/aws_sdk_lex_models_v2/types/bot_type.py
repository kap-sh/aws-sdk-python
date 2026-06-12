"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotType: TypeAlias = Literal[
    "Bot",
    "BotNetwork",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Bot",
        "BotNetwork",
    )
)


def serialize_json(value: BotType) -> str:
    return value


def deserialize_json(data: str) -> BotType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotType value: {data!r}")
    return cast(BotType, data)
