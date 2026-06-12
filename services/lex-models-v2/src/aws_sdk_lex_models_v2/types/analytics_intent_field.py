"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsIntentField: TypeAlias = Literal[
    "IntentName",
    "IntentEndState",
    "IntentLevel",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IntentName",
        "IntentEndState",
        "IntentLevel",
    )
)


def serialize_json(value: AnalyticsIntentField) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsIntentField value: {data!r}")
    return cast(AnalyticsIntentField, data)
