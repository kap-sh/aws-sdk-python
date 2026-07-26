"""Generated from Smithy shape ``com.amazonaws.glue#BackfillErrorCode``."""

from typing import Literal, TypeAlias, cast

BackfillErrorCode: TypeAlias = Literal[
    "ENCRYPTED_PARTITION_ERROR",
    "INTERNAL_ERROR",
    "INVALID_PARTITION_TYPE_DATA_ERROR",
    "MISSING_PARTITION_VALUE_ERROR",
    "UNSUPPORTED_PARTITION_CHARACTER_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackfillErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackfillErrorCode:
    return cast(BackfillErrorCode, data)
