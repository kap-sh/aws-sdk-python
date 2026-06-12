"""Generated from Smithy shape ``com.amazonaws.sfn#TestExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

TestExecutionStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "RETRIABLE",
    "CAUGHT_ERROR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "RETRIABLE",
        "CAUGHT_ERROR",
    )
)


def serialize_aws_json_1_0(value: TestExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TestExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestExecutionStatus value: {data!r}")
    return cast(TestExecutionStatus, data)
