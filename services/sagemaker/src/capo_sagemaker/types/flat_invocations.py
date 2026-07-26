"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlatInvocations``."""

from typing import Literal, TypeAlias, cast

FlatInvocations: TypeAlias = Literal[
    "Continue",
    "Stop",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlatInvocations) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlatInvocations:
    return cast(FlatInvocations, data)
