"""Generated from Smithy shape ``com.amazonaws.quicksight#TransposedTableOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.transposed_table_option

TransposedTableOptionList: TypeAlias = list[
    "aws_sdk_quicksight.types.transposed_table_option.TransposedTableOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransposedTableOptionList) -> list:
    import aws_sdk_quicksight.types.transposed_table_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.transposed_table_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TransposedTableOptionList:
    import aws_sdk_quicksight.types.transposed_table_option

    out: TransposedTableOptionList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.transposed_table_option.deserialize_json(item)
        )
    return out
