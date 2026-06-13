"""Generated from Smithy shape ``com.amazonaws.quicksight#SpecialValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SpecialValue: TypeAlias = Literal[
    "EMPTY",
    "NULL",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMPTY",
        "NULL",
        "OTHER",
    )
)


def serialize_json(value: SpecialValue) -> str:
    return value


def deserialize_json(data: str) -> SpecialValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SpecialValue value: {data!r}")
    return cast(SpecialValue, data)
