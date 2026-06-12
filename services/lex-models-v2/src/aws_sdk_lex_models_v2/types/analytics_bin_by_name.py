"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsBinByName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsBinByName: TypeAlias = Literal[
    "ConversationStartTime",
    "UtteranceTimestamp",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConversationStartTime",
        "UtteranceTimestamp",
    )
)


def serialize_json(value: AnalyticsBinByName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsBinByName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsBinByName value: {data!r}")
    return cast(AnalyticsBinByName, data)
