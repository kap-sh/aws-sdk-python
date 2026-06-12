"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ascending",
        "Descending",
    )
)


def serialize_json(value: AnalyticsSortOrder) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsSortOrder value: {data!r}")
    return cast(AnalyticsSortOrder, data)
