"""Generated from Smithy shape ``com.amazonaws.backup#ScanResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

ScanResourceType: TypeAlias = Literal[
    "EBS",
    "EC2",
    "S3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EBS",
        "EC2",
        "S3",
    )
)


def serialize_json(value: ScanResourceType) -> str:
    return value


def deserialize_json(data: str) -> ScanResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanResourceType value: {data!r}")
    return cast(ScanResourceType, data)
