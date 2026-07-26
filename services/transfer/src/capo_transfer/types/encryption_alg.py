"""Generated from Smithy shape ``com.amazonaws.transfer#EncryptionAlg``."""

from typing import Literal, TypeAlias, cast

EncryptionAlg: TypeAlias = Literal[
    "AES128_CBC",
    "AES192_CBC",
    "AES256_CBC",
    "DES_EDE3_CBC",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionAlg) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionAlg:
    return cast(EncryptionAlg, data)
