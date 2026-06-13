"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ThemeType: TypeAlias = Literal[
    "QUICKSIGHT",
    "CUSTOM",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUICKSIGHT",
        "CUSTOM",
        "ALL",
    )
)


def serialize_json(value: ThemeType) -> str:
    return value


def deserialize_json(data: str) -> ThemeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThemeType value: {data!r}")
    return cast(ThemeType, data)
