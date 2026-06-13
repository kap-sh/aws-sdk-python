"""Generated from Smithy shape ``com.amazonaws.quicksight#NegativeValueDisplayMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NegativeValueDisplayMode: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POSITIVE",
        "NEGATIVE",
    )
)


def serialize_json(value: NegativeValueDisplayMode) -> str:
    return value


def deserialize_json(data: str) -> NegativeValueDisplayMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NegativeValueDisplayMode value: {data!r}")
    return cast(NegativeValueDisplayMode, data)
