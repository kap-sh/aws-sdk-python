"""Generated from Smithy shape ``com.amazonaws.glue#FunctionType``."""

from typing import Literal, TypeAlias, cast

FunctionType: TypeAlias = Literal[
    "REGULAR_FUNCTION",
    "AGGREGATE_FUNCTION",
    "STORED_PROCEDURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FunctionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FunctionType:
    return cast(FunctionType, data)
