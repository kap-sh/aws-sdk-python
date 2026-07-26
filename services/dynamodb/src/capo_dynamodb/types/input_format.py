"""Generated from Smithy shape ``com.amazonaws.dynamodb#InputFormat``."""

from typing import Literal, TypeAlias, cast

InputFormat: TypeAlias = Literal[
    "DYNAMODB_JSON",
    "ION",
    "CSV",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InputFormat:
    return cast(InputFormat, data)
