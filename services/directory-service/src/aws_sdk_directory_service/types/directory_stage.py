"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

DirectoryStage: TypeAlias = Literal[
    "Requested",
    "Creating",
    "Created",
    "Active",
    "Inoperable",
    "Impaired",
    "Restoring",
    "RestoreFailed",
    "Deleting",
    "Deleted",
    "Failed",
    "Updating",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Requested",
        "Creating",
        "Created",
        "Active",
        "Inoperable",
        "Impaired",
        "Restoring",
        "RestoreFailed",
        "Deleting",
        "Deleted",
        "Failed",
        "Updating",
    )
)


def serialize_aws_json_1_1(value: DirectoryStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryStage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DirectoryStage value: {data!r}")
    return cast(DirectoryStage, data)
