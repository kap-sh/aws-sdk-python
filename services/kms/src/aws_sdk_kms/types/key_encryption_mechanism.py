"""Generated from Smithy shape ``com.amazonaws.kms#KeyEncryptionMechanism``."""

from typing import Literal, TypeAlias, cast

KeyEncryptionMechanism: TypeAlias = Literal["RSAES_OAEP_SHA_256",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyEncryptionMechanism) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyEncryptionMechanism:
    return cast(KeyEncryptionMechanism, data)
