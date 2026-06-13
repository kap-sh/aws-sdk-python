"""Generated from Smithy shape ``com.amazonaws.quicksight#ConstantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ConstantType: TypeAlias = Literal[
    "SINGULAR",
    "RANGE",
    "COLLECTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGULAR",
        "RANGE",
        "COLLECTIVE",
    )
)


def serialize_json(value: ConstantType) -> str:
    return value


def deserialize_json(data: str) -> ConstantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConstantType value: {data!r}")
    return cast(ConstantType, data)
