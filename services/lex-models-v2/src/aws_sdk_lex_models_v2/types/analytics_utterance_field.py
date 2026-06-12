"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsUtteranceField: TypeAlias = Literal[
    "UtteranceText",
    "UtteranceState",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UtteranceText",
        "UtteranceState",
    )
)


def serialize_json(value: AnalyticsUtteranceField) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsUtteranceField value: {data!r}")
    return cast(AnalyticsUtteranceField, data)
