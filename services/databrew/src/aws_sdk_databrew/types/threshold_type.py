"""Generated from Smithy shape ``com.amazonaws.databrew#ThresholdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

ThresholdType: TypeAlias = Literal[
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN_OR_EQUAL",
    "GREATER_THAN",
    "LESS_THAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "LESS_THAN",
    )
)


def serialize_json(value: ThresholdType) -> str:
    return value


def deserialize_json(data: str) -> ThresholdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThresholdType value: {data!r}")
    return cast(ThresholdType, data)
