"""Generated from Smithy shape ``com.amazonaws.directoryservice#SnapshotStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

SnapshotStatus: TypeAlias = Literal[
    "Creating",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Completed",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: SnapshotStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotStatus value: {data!r}")
    return cast(SnapshotStatus, data)
