"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CannedAclForObjectsValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

CannedAclForObjectsValue: TypeAlias = Literal[
    "none",
    "private",
    "public-read",
    "public-read-write",
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "private",
        "public-read",
        "public-read-write",
        "authenticated-read",
        "aws-exec-read",
        "bucket-owner-read",
        "bucket-owner-full-control",
    )
)


def serialize_aws_json_1_1(value: CannedAclForObjectsValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CannedAclForObjectsValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CannedAclForObjectsValue value: {data!r}")
    return cast(CannedAclForObjectsValue, data)
