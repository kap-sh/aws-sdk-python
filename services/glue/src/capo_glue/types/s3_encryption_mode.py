"""Generated from Smithy shape ``com.amazonaws.glue#S3EncryptionMode``."""

from typing import Literal, TypeAlias, cast

S3EncryptionMode: TypeAlias = Literal[
    "DISABLED",
    "SSE-KMS",
    "SSE-S3",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3EncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3EncryptionMode:
    return cast(S3EncryptionMode, data)
