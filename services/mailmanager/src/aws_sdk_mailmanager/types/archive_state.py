"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ArchiveState: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_DELETION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PENDING_DELETION",
    )
)


def serialize_aws_json_1_0(value: ArchiveState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArchiveState value: {data!r}")
    return cast(ArchiveState, data)
