"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticTableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_entity_resource_id
    import aws_sdk_quicksight.types.semantic_table

SemanticTableMap: TypeAlias = dict[
    "aws_sdk_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId",
    "aws_sdk_quicksight.types.semantic_table.SemanticTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SemanticTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_quicksight.types.semantic_table

        out[key] = aws_sdk_quicksight.types.semantic_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SemanticTableMap:
    out: SemanticTableMap = {}
    for key, value in data.items():
        import aws_sdk_quicksight.types.semantic_table

        out[key] = aws_sdk_quicksight.types.semantic_table.deserialize_json(value)
    return out
