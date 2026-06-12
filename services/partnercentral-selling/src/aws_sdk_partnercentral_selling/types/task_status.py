"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

TaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETE",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: TaskStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatus value: {data!r}")
    return cast(TaskStatus, data)
