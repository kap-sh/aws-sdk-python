"""Generated from Smithy shape ``com.amazonaws.ecr#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "AES256",
    "KMS",
    "KMS_DSSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
