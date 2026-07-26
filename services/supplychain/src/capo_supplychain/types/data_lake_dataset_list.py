"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset

DataLakeDatasetList: TypeAlias = list[
    "capo_supplychain.types.data_lake_dataset.DataLakeDataset"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetList) -> list:
    import capo_supplychain.types.data_lake_dataset

    out: list = []
    for item in value:
        out.append(capo_supplychain.types.data_lake_dataset.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeDatasetList:
    import capo_supplychain.types.data_lake_dataset

    out: DataLakeDatasetList = []
    for item in data:
        out.append(capo_supplychain.types.data_lake_dataset.deserialize_json(item))
    return out
