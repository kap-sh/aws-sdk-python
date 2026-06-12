"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsNodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsNodeType: TypeAlias = Literal[
    "Inner",
    "Exit",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Inner",
        "Exit",
    )
)


def serialize_json(value: AnalyticsNodeType) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsNodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsNodeType value: {data!r}")
    return cast(AnalyticsNodeType, data)
