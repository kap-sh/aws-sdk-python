"""Generated from Smithy shape ``com.amazonaws.databrew#SheetNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.sheet_name

SheetNameList: TypeAlias = list["aws_sdk_databrew.types.sheet_name.SheetName"]


# --- restJson1 ser/de ---
def serialize_json(value: SheetNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> SheetNameList:
    return list(data)
