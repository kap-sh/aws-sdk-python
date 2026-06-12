"""Generated from Smithy shape ``com.amazonaws.frauddetector#AsyncJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

AsyncJobStatus: TypeAlias = Literal[
    "IN_PROGRESS_INITIALIZING",
    "IN_PROGRESS",
    "CANCEL_IN_PROGRESS",
    "CANCELED",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS_INITIALIZING",
        "IN_PROGRESS",
        "CANCEL_IN_PROGRESS",
        "CANCELED",
        "COMPLETE",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: AsyncJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AsyncJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AsyncJobStatus value: {data!r}")
    return cast(AsyncJobStatus, data)
