"""Generated from Smithy shape ``com.amazonaws.lakeformation#ColumnNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.name_string

ColumnNames: TypeAlias = list["aws_sdk_lakeformation.types.name_string.NameString"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnNames) -> list:
    return list(value)


def deserialize_json(data: list) -> ColumnNames:
    return list(data)
