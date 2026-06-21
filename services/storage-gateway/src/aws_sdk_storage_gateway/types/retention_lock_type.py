"""Generated from Smithy shape ``com.amazonaws.storagegateway#RetentionLockType``."""

from typing import Literal, TypeAlias, cast

RetentionLockType: TypeAlias = Literal[
    "COMPLIANCE",
    "GOVERNANCE",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionLockType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetentionLockType:
    return cast(RetentionLockType, data)
