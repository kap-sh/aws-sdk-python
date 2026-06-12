"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
    "NE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CO",
        "EQ",
        "NE",
    )
)


def serialize_json(value: BotFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> BotFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotFilterOperator value: {data!r}")
    return cast(BotFilterOperator, data)
