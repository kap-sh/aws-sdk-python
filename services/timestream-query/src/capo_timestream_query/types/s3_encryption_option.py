"""Generated from Smithy shape ``com.amazonaws.timestreamquery#S3EncryptionOption``."""

from typing import Literal, TypeAlias, cast

S3EncryptionOption: TypeAlias = Literal[
    "SSE_S3",
    "SSE_KMS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3EncryptionOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> S3EncryptionOption:
    return cast(S3EncryptionOption, data)
