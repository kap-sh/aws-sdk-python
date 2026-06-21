"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetSchemaFieldType``."""

from typing import Literal, TypeAlias, cast

DataLakeDatasetSchemaFieldType: TypeAlias = Literal[
    "INT",
    "DOUBLE",
    "STRING",
    "TIMESTAMP",
    "LONG",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeDatasetSchemaFieldType) -> str:
    return value


def deserialize_json(data: str) -> DataLakeDatasetSchemaFieldType:
    return cast(DataLakeDatasetSchemaFieldType, data)
