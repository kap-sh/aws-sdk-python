"""Generated from Smithy shape ``com.amazonaws.directoryservice#SchemaExtensionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

SchemaExtensionStatus: TypeAlias = Literal[
    "Initializing",
    "CreatingSnapshot",
    "UpdatingSchema",
    "Replicating",
    "CancelInProgress",
    "RollbackInProgress",
    "Cancelled",
    "Failed",
    "Completed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Initializing",
        "CreatingSnapshot",
        "UpdatingSchema",
        "Replicating",
        "CancelInProgress",
        "RollbackInProgress",
        "Cancelled",
        "Failed",
        "Completed",
    )
)


def serialize_aws_json_1_1(value: SchemaExtensionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaExtensionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaExtensionStatus value: {data!r}")
    return cast(SchemaExtensionStatus, data)
