"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseManagementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DatabaseManagementStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "NOT_ENABLED",
    "FAILED_ENABLING",
    "FAILED_DISABLING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "NOT_ENABLED",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
    )
)


def serialize_aws_json_1_0(value: DatabaseManagementStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatabaseManagementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseManagementStatus value: {data!r}")
    return cast(DatabaseManagementStatus, data)
