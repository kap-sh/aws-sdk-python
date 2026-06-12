"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "Queued",
    "InProgress",
    "Complete",
    "Failed",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Queued",
        "InProgress",
        "Complete",
        "Failed",
    )
)


def serialize_aws_json_1_0(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
