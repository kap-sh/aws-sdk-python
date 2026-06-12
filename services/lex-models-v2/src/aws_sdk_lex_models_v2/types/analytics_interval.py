"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsInterval``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsInterval: TypeAlias = Literal[
    "OneHour",
    "OneDay",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OneHour",
        "OneDay",
    )
)


def serialize_json(value: AnalyticsInterval) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsInterval:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsInterval value: {data!r}")
    return cast(AnalyticsInterval, data)
