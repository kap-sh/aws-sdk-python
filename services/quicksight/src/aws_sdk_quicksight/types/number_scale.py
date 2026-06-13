"""Generated from Smithy shape ``com.amazonaws.quicksight#NumberScale``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NumberScale: TypeAlias = Literal[
    "NONE",
    "AUTO",
    "THOUSANDS",
    "MILLIONS",
    "BILLIONS",
    "TRILLIONS",
    "LAKHS",
    "CRORES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "AUTO",
        "THOUSANDS",
        "MILLIONS",
        "BILLIONS",
        "TRILLIONS",
        "LAKHS",
        "CRORES",
    )
)


def serialize_json(value: NumberScale) -> str:
    return value


def deserialize_json(data: str) -> NumberScale:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NumberScale value: {data!r}")
    return cast(NumberScale, data)
