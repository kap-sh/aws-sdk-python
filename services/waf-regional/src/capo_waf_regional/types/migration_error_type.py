"""Generated from Smithy shape ``com.amazonaws.wafregional#MigrationErrorType``."""

from typing import Literal, TypeAlias, cast

MigrationErrorType: TypeAlias = Literal[
    "ENTITY_NOT_SUPPORTED",
    "ENTITY_NOT_FOUND",
    "S3_BUCKET_NO_PERMISSION",
    "S3_BUCKET_NOT_ACCESSIBLE",
    "S3_BUCKET_NOT_FOUND",
    "S3_BUCKET_INVALID_REGION",
    "S3_INTERNAL_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationErrorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MigrationErrorType:
    return cast(MigrationErrorType, data)
