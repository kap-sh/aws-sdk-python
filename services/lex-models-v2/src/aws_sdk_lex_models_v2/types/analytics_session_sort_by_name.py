"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionSortByName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsSessionSortByName: TypeAlias = Literal[
    "ConversationStartTime",
    "NumberOfTurns",
    "Duration",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConversationStartTime",
        "NumberOfTurns",
        "Duration",
    )
)


def serialize_json(value: AnalyticsSessionSortByName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSessionSortByName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsSessionSortByName value: {data!r}"
        )
    return cast(AnalyticsSessionSortByName, data)
