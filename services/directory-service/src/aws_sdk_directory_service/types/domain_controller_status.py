"""Generated from Smithy shape ``com.amazonaws.directoryservice#DomainControllerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

DomainControllerStatus: TypeAlias = Literal[
    "Creating",
    "Active",
    "Impaired",
    "Restoring",
    "Deleting",
    "Deleted",
    "Failed",
    "Updating",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Active",
        "Impaired",
        "Restoring",
        "Deleting",
        "Deleted",
        "Failed",
        "Updating",
    )
)


def serialize_aws_json_1_1(value: DomainControllerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainControllerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainControllerStatus value: {data!r}")
    return cast(DomainControllerStatus, data)
