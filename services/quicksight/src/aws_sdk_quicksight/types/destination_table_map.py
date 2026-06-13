"""Generated from Smithy shape ``com.amazonaws.quicksight#DestinationTableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_entity_resource_id
    import aws_sdk_quicksight.types.destination_table

DestinationTableMap: TypeAlias = dict[
    "aws_sdk_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId",
    "aws_sdk_quicksight.types.destination_table.DestinationTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DestinationTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_quicksight.types.destination_table

        out[key] = aws_sdk_quicksight.types.destination_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> DestinationTableMap:
    out: DestinationTableMap = {}
    for key, value in data.items():
        import aws_sdk_quicksight.types.destination_table

        out[key] = aws_sdk_quicksight.types.destination_table.deserialize_json(value)
    return out
