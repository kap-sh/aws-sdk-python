"""Generated from Smithy shape ``com.amazonaws.kms#KeyState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

KeyState: TypeAlias = Literal[
    "Creating",
    "Enabled",
    "Disabled",
    "PendingDeletion",
    "PendingImport",
    "PendingReplicaDeletion",
    "Unavailable",
    "Updating",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Enabled",
        "Disabled",
        "PendingDeletion",
        "PendingImport",
        "PendingReplicaDeletion",
        "Unavailable",
        "Updating",
    )
)


def serialize_aws_json_1_1(value: KeyState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyState value: {data!r}")
    return cast(KeyState, data)
