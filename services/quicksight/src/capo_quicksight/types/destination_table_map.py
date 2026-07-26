"""Generated from Smithy shape ``com.amazonaws.quicksight#DestinationTableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_entity_resource_id
    import capo_quicksight.types.destination_table

DestinationTableMap: TypeAlias = dict[
    "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId",
    "capo_quicksight.types.destination_table.DestinationTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DestinationTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.destination_table

        out[key] = capo_quicksight.types.destination_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> DestinationTableMap:
    out: DestinationTableMap = {}
    for key, value in data.items():
        import capo_quicksight.types.destination_table

        out[key] = capo_quicksight.types.destination_table.deserialize_json(value)
    return out
