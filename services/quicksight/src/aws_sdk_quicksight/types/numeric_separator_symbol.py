"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericSeparatorSymbol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NumericSeparatorSymbol: TypeAlias = Literal[
    "COMMA",
    "DOT",
    "SPACE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMMA",
        "DOT",
        "SPACE",
    )
)


def serialize_json(value: NumericSeparatorSymbol) -> str:
    return value


def deserialize_json(data: str) -> NumericSeparatorSymbol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NumericSeparatorSymbol value: {data!r}")
    return cast(NumericSeparatorSymbol, data)
