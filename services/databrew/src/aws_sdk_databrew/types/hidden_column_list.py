"""Generated from Smithy shape ``com.amazonaws.databrew#HiddenColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.column_name

HiddenColumnList: TypeAlias = list["aws_sdk_databrew.types.column_name.ColumnName"]


# --- restJson1 ser/de ---
def serialize_json(value: HiddenColumnList) -> list:
    return list(value)


def deserialize_json(data: list) -> HiddenColumnList:
    return list(data)
