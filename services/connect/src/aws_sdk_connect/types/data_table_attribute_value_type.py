"""Generated from Smithy shape ``com.amazonaws.connect#DataTableAttributeValueType``."""

from typing import Literal, TypeAlias, cast

DataTableAttributeValueType: TypeAlias = Literal[
    "TEXT",
    "NUMBER",
    "BOOLEAN",
    "TEXT_LIST",
    "NUMBER_LIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableAttributeValueType) -> str:
    return value


def deserialize_json(data: str) -> DataTableAttributeValueType:
    return cast(DataTableAttributeValueType, data)
