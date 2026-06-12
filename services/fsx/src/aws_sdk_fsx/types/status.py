"""Generated from Smithy shape ``com.amazonaws.fsx#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

Status: TypeAlias = Literal[
    "FAILED",
    "IN_PROGRESS",
    "PENDING",
    "COMPLETED",
    "UPDATED_OPTIMIZING",
    "OPTIMIZING",
    "PAUSED",
    "CANCELLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "IN_PROGRESS",
        "PENDING",
        "COMPLETED",
        "UPDATED_OPTIMIZING",
        "OPTIMIZING",
        "PAUSED",
        "CANCELLED",
    )
)


def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
