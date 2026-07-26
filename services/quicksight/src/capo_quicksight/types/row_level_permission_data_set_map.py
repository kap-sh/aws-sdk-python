"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionDataSetMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_entity_resource_id
    import capo_quicksight.types.row_level_permission_data_set

RowLevelPermissionDataSetMap: TypeAlias = dict[
    "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId",
    "capo_quicksight.types.row_level_permission_data_set.RowLevelPermissionDataSet",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RowLevelPermissionDataSetMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.row_level_permission_data_set

        out[key] = capo_quicksight.types.row_level_permission_data_set.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> RowLevelPermissionDataSetMap:
    out: RowLevelPermissionDataSetMap = {}
    for key, value in data.items():
        import capo_quicksight.types.row_level_permission_data_set

        out[key] = capo_quicksight.types.row_level_permission_data_set.deserialize_json(
            value
        )
    return out
