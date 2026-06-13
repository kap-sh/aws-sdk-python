"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageScalingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SheetImageScalingType: TypeAlias = Literal[
    "SCALE_TO_WIDTH",
    "SCALE_TO_HEIGHT",
    "SCALE_TO_CONTAINER",
    "SCALE_NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCALE_TO_WIDTH",
        "SCALE_TO_HEIGHT",
        "SCALE_TO_CONTAINER",
        "SCALE_NONE",
    )
)


def serialize_json(value: SheetImageScalingType) -> str:
    return value


def deserialize_json(data: str) -> SheetImageScalingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SheetImageScalingType value: {data!r}")
    return cast(SheetImageScalingType, data)
