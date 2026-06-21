"""Generated from Smithy shape ``com.amazonaws.sfn#MockResponseValidationMode``."""

from typing import Literal, TypeAlias, cast

MockResponseValidationMode: TypeAlias = Literal[
    "STRICT",
    "PRESENT",
    "NONE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MockResponseValidationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MockResponseValidationMode:
    return cast(MockResponseValidationMode, data)
