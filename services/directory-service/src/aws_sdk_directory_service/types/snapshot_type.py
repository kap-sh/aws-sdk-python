"""Generated from Smithy shape ``com.amazonaws.directoryservice#SnapshotType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

SnapshotType: TypeAlias = Literal[
    "Auto",
    "Manual",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Auto",
        "Manual",
    )
)


def serialize_aws_json_1_1(value: SnapshotType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotType value: {data!r}")
    return cast(SnapshotType, data)
