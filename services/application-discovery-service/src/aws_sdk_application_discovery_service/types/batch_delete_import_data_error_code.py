"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteImportDataErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchDeleteImportDataErrorCode: TypeAlias = Literal[
    "NOT_FOUND",
    "INTERNAL_SERVER_ERROR",
    "OVER_LIMIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteImportDataErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchDeleteImportDataErrorCode:
    return cast(BatchDeleteImportDataErrorCode, data)
