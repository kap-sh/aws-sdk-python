"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CandidateStatus: TypeAlias = Literal[
    "Completed",
    "InProgress",
    "Failed",
    "Stopped",
    "Stopping",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Completed",
        "InProgress",
        "Failed",
        "Stopped",
        "Stopping",
    )
)


def serialize_aws_json_1_1(value: CandidateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CandidateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CandidateStatus value: {data!r}")
    return cast(CandidateStatus, data)
