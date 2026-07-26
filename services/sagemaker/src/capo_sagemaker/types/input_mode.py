"""Generated from Smithy shape ``com.amazonaws.sagemaker#InputMode``."""

from typing import Literal, TypeAlias, cast

InputMode: TypeAlias = Literal[
    "Pipe",
    "File",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputMode:
    return cast(InputMode, data)
