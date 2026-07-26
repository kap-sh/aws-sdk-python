"""Generated from Smithy shape ``com.amazonaws.sfn#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KMS_KEY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
