"""Generated from Smithy shape ``com.amazonaws.eventbridge#ArchiveState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

ArchiveState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "CREATING",
    "UPDATING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "CREATING",
        "UPDATING",
        "CREATE_FAILED",
        "UPDATE_FAILED",
    )
)


def serialize_aws_json_1_1(value: ArchiveState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArchiveState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArchiveState value: {data!r}")
    return cast(ArchiveState, data)
