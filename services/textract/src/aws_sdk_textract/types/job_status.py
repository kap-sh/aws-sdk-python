"""Generated from Smithy shape ``com.amazonaws.textract#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "PARTIAL_SUCCESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "PARTIAL_SUCCESS",
    )
)


def serialize_aws_json_1_1(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
