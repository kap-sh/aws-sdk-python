"""Generated from Smithy shape ``com.amazonaws.quicksight#ColorFillType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ColorFillType: TypeAlias = Literal[
    "DISCRETE",
    "GRADIENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISCRETE",
        "GRADIENT",
    )
)


def serialize_json(value: ColorFillType) -> str:
    return value


def deserialize_json(data: str) -> ColorFillType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColorFillType value: {data!r}")
    return cast(ColorFillType, data)
