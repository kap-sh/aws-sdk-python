"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

BatchLoadStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
    "PROGRESS_STOPPED",
    "PENDING_RESUME",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
        "PROGRESS_STOPPED",
        "PENDING_RESUME",
    )
)


def serialize_aws_json_1_0(value: BatchLoadStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchLoadStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchLoadStatus value: {data!r}")
    return cast(BatchLoadStatus, data)
