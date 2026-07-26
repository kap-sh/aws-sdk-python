"""Generated from Smithy shape ``com.amazonaws.sfn#TestExecutionStatus``."""

from typing import Literal, TypeAlias, cast

TestExecutionStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "RETRIABLE",
    "CAUGHT_ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TestExecutionStatus:
    return cast(TestExecutionStatus, data)
