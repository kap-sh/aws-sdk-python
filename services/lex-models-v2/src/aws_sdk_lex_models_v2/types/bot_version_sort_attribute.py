"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotVersionSortAttribute: TypeAlias = Literal["BotVersion",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BotVersion",))


def serialize_json(value: BotVersionSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BotVersionSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotVersionSortAttribute value: {data!r}")
    return cast(BotVersionSortAttribute, data)
