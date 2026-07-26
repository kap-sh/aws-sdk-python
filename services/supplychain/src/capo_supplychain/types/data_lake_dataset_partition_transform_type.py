"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPartitionTransformType``."""

from typing import Literal, TypeAlias, cast

DataLakeDatasetPartitionTransformType: TypeAlias = Literal[
    "YEAR",
    "MONTH",
    "DAY",
    "HOUR",
    "IDENTITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetPartitionTransformType) -> str:
    return value


def deserialize_json(data: str) -> DataLakeDatasetPartitionTransformType:
    return cast(DataLakeDatasetPartitionTransformType, data)
