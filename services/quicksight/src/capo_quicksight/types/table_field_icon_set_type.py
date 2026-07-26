"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldIconSetType``."""

from typing import Literal, TypeAlias, cast

TableFieldIconSetType: TypeAlias = Literal["LINK",]


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldIconSetType) -> str:
    return value


def deserialize_json(data: str) -> TableFieldIconSetType:
    return cast(TableFieldIconSetType, data)
