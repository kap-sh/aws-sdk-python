"""Generated from Smithy shape ``com.amazonaws.inspector#FailedItemErrorCode``."""

from typing import Literal, TypeAlias, cast

FailedItemErrorCode: TypeAlias = Literal[
    "INVALID_ARN",
    "DUPLICATE_ARN",
    "ITEM_DOES_NOT_EXIST",
    "ACCESS_DENIED",
    "LIMIT_EXCEEDED",
    "INTERNAL_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedItemErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailedItemErrorCode:
    return cast(FailedItemErrorCode, data)
