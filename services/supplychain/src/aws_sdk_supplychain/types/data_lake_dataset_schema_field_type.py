"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetSchemaFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataLakeDatasetSchemaFieldType: TypeAlias = Literal[
    "INT",
    "DOUBLE",
    "STRING",
    "TIMESTAMP",
    "LONG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INT",
        "DOUBLE",
        "STRING",
        "TIMESTAMP",
        "LONG",
    )
)


def serialize_json(value: DataLakeDatasetSchemaFieldType) -> str:
    return value


def deserialize_json(data: str) -> DataLakeDatasetSchemaFieldType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataLakeDatasetSchemaFieldType value: {data!r}"
        )
    return cast(DataLakeDatasetSchemaFieldType, data)
