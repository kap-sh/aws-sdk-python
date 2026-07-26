"""Generated from Smithy shape ``com.amazonaws.quicksight#SourceTableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_entity_resource_id
    import capo_quicksight.types.source_table

SourceTableMap: TypeAlias = dict[
    "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId",
    "capo_quicksight.types.source_table.SourceTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SourceTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.source_table

        out[key] = capo_quicksight.types.source_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SourceTableMap:
    out: SourceTableMap = {}
    for key, value in data.items():
        import capo_quicksight.types.source_table

        out[key] = capo_quicksight.types.source_table.deserialize_json(value)
    return out
