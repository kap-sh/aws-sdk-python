"""Generated from Smithy shape ``com.amazonaws.databrew#AnalyticsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

AnalyticsMode: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE",
        "DISABLE",
    )
)


def serialize_json(value: AnalyticsMode) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsMode value: {data!r}")
    return cast(AnalyticsMode, data)
