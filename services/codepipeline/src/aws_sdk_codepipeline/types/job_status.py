"""Generated from Smithy shape ``com.amazonaws.codepipeline#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "Created",
    "Queued",
    "Dispatched",
    "InProgress",
    "TimedOut",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Created",
        "Queued",
        "Dispatched",
        "InProgress",
        "TimedOut",
        "Succeeded",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
