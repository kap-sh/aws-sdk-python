"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsSessionField: TypeAlias = Literal[
    "ConversationEndState",
    "LocaleId",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConversationEndState",
        "LocaleId",
    )
)


def serialize_json(value: AnalyticsSessionField) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSessionField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsSessionField value: {data!r}")
    return cast(AnalyticsSessionField, data)
