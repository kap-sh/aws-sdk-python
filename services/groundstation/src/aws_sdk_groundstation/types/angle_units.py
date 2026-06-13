"""Generated from Smithy shape ``com.amazonaws.groundstation#AngleUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

AngleUnits: TypeAlias = Literal[
    "DEGREE_ANGLE",
    "RADIAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEGREE_ANGLE",
        "RADIAN",
    )
)


def serialize_json(value: AngleUnits) -> str:
    return value


def deserialize_json(data: str) -> AngleUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AngleUnits value: {data!r}")
    return cast(AngleUnits, data)
