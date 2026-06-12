"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ReplicationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETE",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ReplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicationStatus value: {data!r}")
    return cast(ReplicationStatus, data)
