"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPrimaryKeyFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_primary_key_field

DataLakeDatasetPrimaryKeyFieldList: TypeAlias = list[
    "capo_supplychain.types.data_lake_dataset_primary_key_field.DataLakeDatasetPrimaryKeyField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetPrimaryKeyFieldList) -> list:
    import capo_supplychain.types.data_lake_dataset_primary_key_field

    out: list = []
    for item in value:
        out.append(
            capo_supplychain.types.data_lake_dataset_primary_key_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataLakeDatasetPrimaryKeyFieldList:
    import capo_supplychain.types.data_lake_dataset_primary_key_field

    out: DataLakeDatasetPrimaryKeyFieldList = []
    for item in data:
        out.append(
            capo_supplychain.types.data_lake_dataset_primary_key_field.deserialize_json(
                item
            )
        )
    return out
