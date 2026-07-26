"""Generated from Smithy shape ``com.amazonaws.athena#EncryptionOption``."""

from typing import Literal, TypeAlias, cast

EncryptionOption: TypeAlias = Literal[
    "SSE_S3",
    "SSE_KMS",
    "CSE_KMS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionOption:
    return cast(EncryptionOption, data)
