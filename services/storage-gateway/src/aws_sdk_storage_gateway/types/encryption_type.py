"""Generated from Smithy shape ``com.amazonaws.storagegateway#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "SseS3",
    "SseKms",
    "DsseKms",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
