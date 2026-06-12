"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SafeguardPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

SafeguardPolicy: TypeAlias = Literal[
    "rely-on-sql-server-replication-agent",
    "exclusive-automatic-truncation",
    "shared-automatic-truncation",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "rely-on-sql-server-replication-agent",
        "exclusive-automatic-truncation",
        "shared-automatic-truncation",
    )
)


def serialize_aws_json_1_1(value: SafeguardPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SafeguardPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SafeguardPolicy value: {data!r}")
    return cast(SafeguardPolicy, data)
