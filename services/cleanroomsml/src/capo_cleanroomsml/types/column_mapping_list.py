"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ColumnMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.synthetic_data_column_properties

ColumnMappingList: TypeAlias = list[
    "capo_cleanroomsml.types.synthetic_data_column_properties.SyntheticDataColumnProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnMappingList) -> list:
    import capo_cleanroomsml.types.synthetic_data_column_properties

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.synthetic_data_column_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ColumnMappingList:
    import capo_cleanroomsml.types.synthetic_data_column_properties

    out: ColumnMappingList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.synthetic_data_column_properties.deserialize_json(
                item
            )
        )
    return out
