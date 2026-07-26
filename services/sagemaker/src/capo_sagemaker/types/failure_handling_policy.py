"""Generated from Smithy shape ``com.amazonaws.sagemaker#FailureHandlingPolicy``."""

from typing import Literal, TypeAlias, cast

FailureHandlingPolicy: TypeAlias = Literal[
    "ROLLBACK_ON_FAILURE",
    "DO_NOTHING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureHandlingPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureHandlingPolicy:
    return cast(FailureHandlingPolicy, data)
