"""Generated from Smithy shape ``com.amazonaws.databrew#ThresholdUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

ThresholdUnit: TypeAlias = Literal[
    "COUNT",
    "PERCENTAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COUNT",
        "PERCENTAGE",
    )
)


def serialize_json(value: ThresholdUnit) -> str:
    return value


def deserialize_json(data: str) -> ThresholdUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThresholdUnit value: {data!r}")
    return cast(ThresholdUnit, data)
