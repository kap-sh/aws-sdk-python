"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionKeyProvider``."""

from typing import Literal, TypeAlias, cast

EncryptionKeyProvider: TypeAlias = Literal[
    "ORACLE_MANAGED",
    "AWS_KMS",
    "OKV",
    "OCI",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionKeyProvider) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionKeyProvider:
    return cast(EncryptionKeyProvider, data)
