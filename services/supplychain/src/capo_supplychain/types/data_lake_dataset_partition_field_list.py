"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPartitionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_partition_field

DataLakeDatasetPartitionFieldList: TypeAlias = list[
    "capo_supplychain.types.data_lake_dataset_partition_field.DataLakeDatasetPartitionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetPartitionFieldList) -> list:
    import capo_supplychain.types.data_lake_dataset_partition_field

    out: list = []
    for item in value:
        out.append(
            capo_supplychain.types.data_lake_dataset_partition_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataLakeDatasetPartitionFieldList:
    import capo_supplychain.types.data_lake_dataset_partition_field

    out: DataLakeDatasetPartitionFieldList = []
    for item in data:
        out.append(
            capo_supplychain.types.data_lake_dataset_partition_field.deserialize_json(
                item
            )
        )
    return out
