"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatePartitionSequenceValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

DatePartitionSequenceValue: TypeAlias = Literal[
    "YYYYMMDD",
    "YYYYMMDDHH",
    "YYYYMM",
    "MMYYYYDD",
    "DDMMYYYY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "YYYYMMDD",
        "YYYYMMDDHH",
        "YYYYMM",
        "MMYYYYDD",
        "DDMMYYYY",
    )
)


def serialize_aws_json_1_1(value: DatePartitionSequenceValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatePartitionSequenceValue:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DatePartitionSequenceValue value: {data!r}"
        )
    return cast(DatePartitionSequenceValue, data)
