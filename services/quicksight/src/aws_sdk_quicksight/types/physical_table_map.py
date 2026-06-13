"""Generated from Smithy shape ``com.amazonaws.quicksight#PhysicalTableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.physical_table
    import aws_sdk_quicksight.types.physical_table_id

PhysicalTableMap: TypeAlias = dict[
    "aws_sdk_quicksight.types.physical_table_id.PhysicalTableId",
    "aws_sdk_quicksight.types.physical_table.PhysicalTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PhysicalTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_quicksight.types.physical_table

        out[key] = aws_sdk_quicksight.types.physical_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PhysicalTableMap:
    out: PhysicalTableMap = {}
    for key, value in data.items():
        import aws_sdk_quicksight.types.physical_table

        out[key] = aws_sdk_quicksight.types.physical_table.deserialize_json(value)
    return out
