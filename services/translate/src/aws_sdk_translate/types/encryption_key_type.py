"""Generated from Smithy shape ``com.amazonaws.translate#EncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

EncryptionKeyType: TypeAlias = Literal["KMS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionKeyType:
    return cast(EncryptionKeyType, data)
