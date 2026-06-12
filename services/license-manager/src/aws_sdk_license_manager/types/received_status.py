"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReceivedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

ReceivedStatus: TypeAlias = Literal[
    "PENDING_WORKFLOW",
    "PENDING_ACCEPT",
    "REJECTED",
    "ACTIVE",
    "FAILED_WORKFLOW",
    "DELETED",
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
        "DISABLED",
        "WORKFLOW_COMPLETED",
    )
)


def serialize_aws_json_1_1(value: ReceivedStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReceivedStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReceivedStatus value: {data!r}")
    return cast(ReceivedStatus, data)
