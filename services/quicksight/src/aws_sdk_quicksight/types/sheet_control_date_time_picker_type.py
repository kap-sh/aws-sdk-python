"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlDateTimePickerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SheetControlDateTimePickerType: TypeAlias = Literal[
    "SINGLE_VALUED",
    "DATE_RANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_VALUED",
        "DATE_RANGE",
    )
)


def serialize_json(value: SheetControlDateTimePickerType) -> str:
    return value


def deserialize_json(data: str) -> SheetControlDateTimePickerType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SheetControlDateTimePickerType value: {data!r}"
        )
    return cast(SheetControlDateTimePickerType, data)
