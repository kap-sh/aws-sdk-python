"""Generated from Smithy shape ``com.amazonaws.quicksight#PropertyUsage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PropertyUsage: TypeAlias = Literal[
    "INHERIT",
    "DIMENSION",
    "MEASURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INHERIT",
        "DIMENSION",
        "MEASURE",
    )
)


def serialize_json(value: PropertyUsage) -> str:
    return value


def deserialize_json(data: str) -> PropertyUsage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropertyUsage value: {data!r}")
    return cast(PropertyUsage, data)
