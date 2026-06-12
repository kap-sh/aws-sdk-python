"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotSortAttribute: TypeAlias = Literal["BotName",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BotName",))


def serialize_json(value: BotSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BotSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotSortAttribute value: {data!r}")
    return cast(BotSortAttribute, data)
