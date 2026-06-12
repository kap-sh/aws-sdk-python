"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CollectorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

CollectorStatus: TypeAlias = Literal[
    "UNREGISTERED",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNREGISTERED",
        "ACTIVE",
    )
)


def serialize_aws_json_1_1(value: CollectorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CollectorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CollectorStatus value: {data!r}")
    return cast(CollectorStatus, data)
