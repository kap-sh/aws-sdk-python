"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTagNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_tag_name

ColumnTagNames: TypeAlias = list[
    "aws_sdk_quicksight.types.column_tag_name.ColumnTagName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTagNames) -> list:
    import aws_sdk_quicksight.types.column_tag_name

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.column_tag_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnTagNames:
    import aws_sdk_quicksight.types.column_tag_name

    out: ColumnTagNames = []
    for item in data:
        out.append(aws_sdk_quicksight.types.column_tag_name.deserialize_json(item))
    return out
