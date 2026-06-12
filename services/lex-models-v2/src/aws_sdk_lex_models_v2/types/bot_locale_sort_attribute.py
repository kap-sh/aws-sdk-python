"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotLocaleSortAttribute: TypeAlias = Literal["BotLocaleName",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BotLocaleName",))


def serialize_json(value: BotLocaleSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BotLocaleSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotLocaleSortAttribute value: {data!r}")
    return cast(BotLocaleSortAttribute, data)
