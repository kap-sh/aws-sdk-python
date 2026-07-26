"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlDateTimePickerType``."""

from typing import Literal, TypeAlias, cast

SheetControlDateTimePickerType: TypeAlias = Literal[
    "SINGLE_VALUED",
    "DATE_RANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlDateTimePickerType) -> str:
    return value


def deserialize_json(data: str) -> SheetControlDateTimePickerType:
    return cast(SheetControlDateTimePickerType, data)
