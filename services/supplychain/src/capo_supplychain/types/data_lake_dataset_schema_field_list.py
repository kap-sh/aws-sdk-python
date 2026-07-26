"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetSchemaFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_schema_field

DataLakeDatasetSchemaFieldList: TypeAlias = list[
    "capo_supplychain.types.data_lake_dataset_schema_field.DataLakeDatasetSchemaField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetSchemaFieldList) -> list:
    import capo_supplychain.types.data_lake_dataset_schema_field

    out: list = []
    for item in value:
        out.append(
            capo_supplychain.types.data_lake_dataset_schema_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataLakeDatasetSchemaFieldList:
    import capo_supplychain.types.data_lake_dataset_schema_field

    out: DataLakeDatasetSchemaFieldList = []
    for item in data:
        out.append(
            capo_supplychain.types.data_lake_dataset_schema_field.deserialize_json(item)
        )
    return out
