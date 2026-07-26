"""Generated from Smithy shape ``com.amazonaws.mediastore#MethodName``."""

from typing import Literal, TypeAlias, cast

MethodName: TypeAlias = Literal[
    "PUT",
    "GET",
    "DELETE",
    "HEAD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MethodName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MethodName:
    return cast(MethodName, data)
