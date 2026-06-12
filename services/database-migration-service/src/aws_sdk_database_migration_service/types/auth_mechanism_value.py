"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AuthMechanismValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

AuthMechanismValue: TypeAlias = Literal[
    "default",
    "mongodb_cr",
    "scram_sha_1",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "mongodb_cr",
        "scram_sha_1",
    )
)


def serialize_aws_json_1_1(value: AuthMechanismValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthMechanismValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthMechanismValue value: {data!r}")
    return cast(AuthMechanismValue, data)
