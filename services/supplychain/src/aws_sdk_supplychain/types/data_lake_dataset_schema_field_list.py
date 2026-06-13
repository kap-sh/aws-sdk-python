"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetSchemaFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_dataset_schema_field

DataLakeDatasetSchemaFieldList: TypeAlias = list[
    "aws_sdk_supplychain.types.data_lake_dataset_schema_field.DataLakeDatasetSchemaField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetSchemaFieldList) -> list:
    import aws_sdk_supplychain.types.data_lake_dataset_schema_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_supplychain.types.data_lake_dataset_schema_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataLakeDatasetSchemaFieldList:
    import aws_sdk_supplychain.types.data_lake_dataset_schema_field

    out: DataLakeDatasetSchemaFieldList = []
    for item in data:
        out.append(
            aws_sdk_supplychain.types.data_lake_dataset_schema_field.deserialize_json(
                item
            )
        )
    return out
