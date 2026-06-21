"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionKeyProviderInput``."""

from typing import Literal, TypeAlias, cast

EncryptionKeyProviderInput: TypeAlias = Literal[
    "ORACLE_MANAGED",
    "AWS_KMS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionKeyProviderInput) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionKeyProviderInput:
    return cast(EncryptionKeyProviderInput, data)
