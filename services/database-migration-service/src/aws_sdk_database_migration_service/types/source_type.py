"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

SourceType: TypeAlias = Literal["replication-instance",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("replication-instance",))


def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {data!r}")
    return cast(SourceType, data)
