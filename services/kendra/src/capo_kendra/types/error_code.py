"""Generated from Smithy shape ``com.amazonaws.kendra#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "InternalError",
    "InvalidRequest",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
