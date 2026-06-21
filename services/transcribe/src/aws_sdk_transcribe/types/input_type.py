"""Generated from Smithy shape ``com.amazonaws.transcribe#InputType``."""

from typing import Literal, TypeAlias, cast

InputType: TypeAlias = Literal[
    "REAL_TIME",
    "POST_CALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputType:
    return cast(InputType, data)
