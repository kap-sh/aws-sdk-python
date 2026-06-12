"""Generated from Smithy shape ``com.amazonaws.databrew#SheetIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.sheet_index

SheetIndexList: TypeAlias = list["aws_sdk_databrew.types.sheet_index.SheetIndex"]


# --- restJson1 ser/de ---
def serialize_json(value: SheetIndexList) -> list:
    return list(value)


def deserialize_json(data: list) -> SheetIndexList:
    return list(data)
