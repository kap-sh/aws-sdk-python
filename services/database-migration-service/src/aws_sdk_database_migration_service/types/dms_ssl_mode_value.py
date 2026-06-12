"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DmsSslModeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

DmsSslModeValue: TypeAlias = Literal[
    "none",
    "require",
    "verify-ca",
    "verify-full",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "require",
        "verify-ca",
        "verify-full",
    )
)


def serialize_aws_json_1_1(value: DmsSslModeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DmsSslModeValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DmsSslModeValue value: {data!r}")
    return cast(DmsSslModeValue, data)
