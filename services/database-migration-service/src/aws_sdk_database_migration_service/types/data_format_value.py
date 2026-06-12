"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataFormatValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

DataFormatValue: TypeAlias = Literal[
    "csv",
    "parquet",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "csv",
        "parquet",
    )
)


def serialize_aws_json_1_1(value: DataFormatValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataFormatValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataFormatValue value: {data!r}")
    return cast(DataFormatValue, data)
