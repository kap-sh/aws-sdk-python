"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#BackupState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm_v2.errors import DeserializationError

BackupState: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "READY",
    "DELETED",
    "PENDING_DELETION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "READY",
        "DELETED",
        "PENDING_DELETION",
    )
)


def serialize_aws_json_1_1(value: BackupState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupState value: {data!r}")
    return cast(BackupState, data)
