"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsFilterOperator: TypeAlias = Literal[
    "EQ",
    "GT",
    "LT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "GT",
        "LT",
    )
)


def serialize_json(value: AnalyticsFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsFilterOperator value: {data!r}")
    return cast(AnalyticsFilterOperator, data)
