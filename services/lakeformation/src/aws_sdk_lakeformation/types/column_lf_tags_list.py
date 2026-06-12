"""Generated from Smithy shape ``com.amazonaws.lakeformation#ColumnLFTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.column_lf_tag

ColumnLFTagsList: TypeAlias = list[
    "aws_sdk_lakeformation.types.column_lf_tag.ColumnLFTag"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnLFTagsList) -> list:
    import aws_sdk_lakeformation.types.column_lf_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.column_lf_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnLFTagsList:
    import aws_sdk_lakeformation.types.column_lf_tag

    out: ColumnLFTagsList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.column_lf_tag.deserialize_json(item))
    return out
