"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotLocaleFilterName: TypeAlias = Literal["BotLocaleName",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BotLocaleName",))


def serialize_json(value: BotLocaleFilterName) -> str:
    return value


def deserialize_json(data: str) -> BotLocaleFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotLocaleFilterName value: {data!r}")
    return cast(BotLocaleFilterName, data)
