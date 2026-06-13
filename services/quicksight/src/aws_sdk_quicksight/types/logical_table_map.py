"""Generated from Smithy shape ``com.amazonaws.quicksight#LogicalTableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.logical_table
    import aws_sdk_quicksight.types.logical_table_id

LogicalTableMap: TypeAlias = dict[
    "aws_sdk_quicksight.types.logical_table_id.LogicalTableId",
    "aws_sdk_quicksight.types.logical_table.LogicalTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LogicalTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_quicksight.types.logical_table

        out[key] = aws_sdk_quicksight.types.logical_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LogicalTableMap:
    out: LogicalTableMap = {}
    for key, value in data.items():
        import aws_sdk_quicksight.types.logical_table

        out[key] = aws_sdk_quicksight.types.logical_table.deserialize_json(value)
    return out
