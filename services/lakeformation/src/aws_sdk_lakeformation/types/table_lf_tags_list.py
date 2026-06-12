"""Generated from Smithy shape ``com.amazonaws.lakeformation#TableLFTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.tagged_table

TableLFTagsList: TypeAlias = list[
    "aws_sdk_lakeformation.types.tagged_table.TaggedTable"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableLFTagsList) -> list:
    import aws_sdk_lakeformation.types.tagged_table

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.tagged_table.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableLFTagsList:
    import aws_sdk_lakeformation.types.tagged_table

    out: TableLFTagsList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.tagged_table.deserialize_json(item))
    return out
