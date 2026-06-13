"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

RecoveryPointStatus: TypeAlias = Literal[
    "COMPLETED",
    "PARTIAL",
    "DELETING",
    "EXPIRED",
    "AVAILABLE",
    "STOPPED",
    "CREATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "PARTIAL",
        "DELETING",
        "EXPIRED",
        "AVAILABLE",
        "STOPPED",
        "CREATING",
    )
)


def serialize_json(value: RecoveryPointStatus) -> str:
    return value


def deserialize_json(data: str) -> RecoveryPointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecoveryPointStatus value: {data!r}")
    return cast(RecoveryPointStatus, data)
