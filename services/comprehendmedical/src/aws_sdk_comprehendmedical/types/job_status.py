"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "COMPLETED",
    "PARTIAL_SUCCESS",
    "FAILED",
    "STOP_REQUESTED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "IN_PROGRESS",
        "COMPLETED",
        "PARTIAL_SUCCESS",
        "FAILED",
        "STOP_REQUESTED",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
