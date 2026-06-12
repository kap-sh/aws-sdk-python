"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotLocaleFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CO",
        "EQ",
    )
)


def serialize_json(value: BotLocaleFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> BotLocaleFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotLocaleFilterOperator value: {data!r}")
    return cast(BotLocaleFilterOperator, data)
