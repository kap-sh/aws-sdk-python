"""Generated from Smithy shape ``com.amazonaws.quicksight#DigitGroupingStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DigitGroupingStyle: TypeAlias = Literal[
    "DEFAULT",
    "LAKHS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "LAKHS",
    )
)


def serialize_json(value: DigitGroupingStyle) -> str:
    return value


def deserialize_json(data: str) -> DigitGroupingStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DigitGroupingStyle value: {data!r}")
    return cast(DigitGroupingStyle, data)
