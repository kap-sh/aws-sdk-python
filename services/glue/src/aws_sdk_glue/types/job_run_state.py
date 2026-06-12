"""Generated from Smithy shape ``com.amazonaws.glue#JobRunState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

JobRunState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "SUCCEEDED",
    "FAILED",
    "TIMEOUT",
    "ERROR",
    "WAITING",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "SUCCEEDED",
        "FAILED",
        "TIMEOUT",
        "ERROR",
        "WAITING",
        "EXPIRED",
    )
)


def serialize_aws_json_1_1(value: JobRunState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobRunState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobRunState value: {data!r}")
    return cast(JobRunState, data)
