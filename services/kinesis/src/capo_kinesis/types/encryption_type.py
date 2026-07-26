"""Generated from Smithy shape ``com.amazonaws.kinesis#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "NONE",
    "KMS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
