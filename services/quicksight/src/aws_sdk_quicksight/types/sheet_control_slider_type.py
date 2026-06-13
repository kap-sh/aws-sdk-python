"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlSliderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SheetControlSliderType: TypeAlias = Literal[
    "SINGLE_POINT",
    "RANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_POINT",
        "RANGE",
    )
)


def serialize_json(value: SheetControlSliderType) -> str:
    return value


def deserialize_json(data: str) -> SheetControlSliderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SheetControlSliderType value: {data!r}")
    return cast(SheetControlSliderType, data)
