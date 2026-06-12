"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotFilterName: TypeAlias = Literal[
    "BotName",
    "BotType",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BotName",
        "BotType",
    )
)


def serialize_json(value: BotFilterName) -> str:
    return value


def deserialize_json(data: str) -> BotFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotFilterName value: {data!r}")
    return cast(BotFilterName, data)
