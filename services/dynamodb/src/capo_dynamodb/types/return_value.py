"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReturnValue``."""

from typing import Literal, TypeAlias, cast

ReturnValue: TypeAlias = Literal[
    "NONE",
    "ALL_OLD",
    "UPDATED_OLD",
    "ALL_NEW",
    "UPDATED_NEW",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReturnValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReturnValue:
    return cast(ReturnValue, data)
