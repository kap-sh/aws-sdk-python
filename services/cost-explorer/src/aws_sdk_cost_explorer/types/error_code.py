"""Generated from Smithy shape ``com.amazonaws.costexplorer#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "NO_USAGE_FOUND",
    "INTERNAL_FAILURE",
    "INVALID_SAVINGS_PLANS_TO_ADD",
    "INVALID_SAVINGS_PLANS_TO_EXCLUDE",
    "INVALID_ACCOUNT_ID",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
