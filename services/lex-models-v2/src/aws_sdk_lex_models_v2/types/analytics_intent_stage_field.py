"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsIntentStageField: TypeAlias = Literal[
    "IntentStageName",
    "SwitchedToIntent",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IntentStageName",
        "SwitchedToIntent",
    )
)


def serialize_json(value: AnalyticsIntentStageField) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentStageField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsIntentStageField value: {data!r}")
    return cast(AnalyticsIntentStageField, data)
