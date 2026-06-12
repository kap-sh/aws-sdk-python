"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ParquetVersionValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

ParquetVersionValue: TypeAlias = Literal[
    "parquet-1-0",
    "parquet-2-0",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "parquet-1-0",
        "parquet-2-0",
    )
)


def serialize_aws_json_1_1(value: ParquetVersionValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParquetVersionValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParquetVersionValue value: {data!r}")
    return cast(ParquetVersionValue, data)
