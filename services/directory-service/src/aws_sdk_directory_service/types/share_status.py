"""Generated from Smithy shape ``com.amazonaws.directoryservice#ShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

ShareStatus: TypeAlias = Literal[
    "Shared",
    "PendingAcceptance",
    "Rejected",
    "Rejecting",
    "RejectFailed",
    "Sharing",
    "ShareFailed",
    "Deleted",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Shared",
        "PendingAcceptance",
        "Rejected",
        "Rejecting",
        "RejectFailed",
        "Sharing",
        "ShareFailed",
        "Deleted",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: ShareStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShareStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareStatus value: {data!r}")
    return cast(ShareStatus, data)
