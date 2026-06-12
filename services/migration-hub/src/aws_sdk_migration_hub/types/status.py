"""Generated from Smithy shape ``com.amazonaws.migrationhub#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_migration_hub.errors import DeserializationError

Status: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
