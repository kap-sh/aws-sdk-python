"""Generated from Smithy shape ``com.amazonaws.licensemanager#GrantStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

GrantStatus: TypeAlias = Literal[
    "PENDING_WORKFLOW",
    "PENDING_ACCEPT",
    "REJECTED",
    "ACTIVE",
    "FAILED_WORKFLOW",
    "DELETED",
    "PENDING_DELETE",
    "DISABLED",
    "WORKFLOW_COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_WORKFLOW",
        "PENDING_ACCEPT",
        "REJECTED",
        "ACTIVE",
        "FAILED_WORKFLOW",
        "DELETED",
        "PENDING_DELETE",
        "DISABLED",
        "WORKFLOW_COMPLETED",
    )
)


def serialize_aws_json_1_1(value: GrantStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GrantStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GrantStatus value: {data!r}")
    return cast(GrantStatus, data)
